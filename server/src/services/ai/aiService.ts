import { AIProvider, AIChatRequest, AIChatResponse, AIResponseType, AIMessage } from './aiProvider';
import { GroqProvider } from './groqProvider';
import { GeminiProvider } from './geminiProvider';
import { MistralProvider } from './mistralProvider';
import { MockAIProvider } from './mockAIProvider';
import { QuestionRepository } from '../questionRepository';

export interface AIServiceOptions {
  providers?: Record<string, AIProvider>;
  defaultProvider?: string;
  fallbackOrder?: string[];
  questionRepository?: QuestionRepository;
}

export interface UserAIQuery {
  questionId: string;
  message: string;
  currentEditorCode?: string; // Monaco editor source of truth
  originalBuggyCode?: string;
  lastRunCode?: string;
  codeChangesDiff?: string;
  latestExecutionResult?: {
    status?: string;
    passedCount?: number;
    totalCount?: number;
    compileOutput?: string;
    runtimeOutput?: string;
    errorDetails?: string;
    testResultsSummary?: string;
  };
  userCode?: string; // backward-compatibility alias
  executionOutput?: string; // backward-compatibility alias
  language?: string;
  mode?: 'practice' | 'exam';
  isSubmitted?: boolean;
  type?: AIResponseType;
  history?: AIMessage[];
}

export class AIService {
  private providers: Map<string, AIProvider> = new Map();
  private customDefaultProviderName?: string;
  private customFallbackOrder?: string[];
  private questionRepo: QuestionRepository;

  constructor(options?: AIServiceOptions) {
    this.questionRepo = options?.questionRepository || new QuestionRepository();

    // Register providers
    if (options?.providers) {
      for (const [name, provider] of Object.entries(options.providers)) {
        this.providers.set(name.toLowerCase(), provider);
      }
    } else {
      this.providers.set('groq', new GroqProvider());
      this.providers.set('gemini', new GeminiProvider());
      this.providers.set('mistral', new MistralProvider());
      this.providers.set('mock', new MockAIProvider());
    }

    this.customDefaultProviderName = options?.defaultProvider;
    this.customFallbackOrder = options?.fallbackOrder;
  }

  private getDefaultProviderName(): string {
    return (this.customDefaultProviderName || process.env.AI_PROVIDER || 'groq').toLowerCase();
  }

  private getFallbackOrder(): string[] {
    if (this.customFallbackOrder) {
      const list = [...this.customFallbackOrder];
      if (!list.includes('mock')) list.push('mock');
      return list;
    }

    const envOrder = process.env.AI_FALLBACK_ORDER
      ? process.env.AI_FALLBACK_ORDER.split(',').map(s => s.trim().toLowerCase())
      : ['groq', 'gemini', 'mistral'];

    const order = [...envOrder];
    if (!order.includes('mock')) {
      order.push('mock');
    }
    return order;
  }

  /**
   * Returns current provider status and configured fallback order without exposing API keys.
   */
  public getStatus(): {
    primaryProvider: string;
    fallbackOrder: string[];
    availableProviders: { name: string; configured: boolean }[];
  } {
    const availableProviders = Array.from(this.providers.entries()).map(([name, provider]) => ({
      name,
      configured: provider.isConfigured()
    }));

    return {
      primaryProvider: this.getDefaultProviderName(),
      fallbackOrder: this.getFallbackOrder(),
      availableProviders
    };
  }

  /**
   * Sanitizes and builds the system & user prompts ensuring strict Exam Mode,
   * Monaco editor code primacy, code change tracking, and latest execution result awareness.
   */
  private buildPromptMessages(query: UserAIQuery): { messages: AIMessage[]; questionContext: AIChatRequest['questionContext'] } {
    const q = this.questionRepo.getById(query.questionId, false);
    const mode = query.mode || 'practice';
    const isSubmitted = Boolean(query.isSubmitted);
    const lang = (query.language || 'cpp').toLowerCase();
    const title = q?.title || 'Algorithm Debugging';
    const topic = q?.topic || 'DSA';
    const problemStatement = q?.problemStatement || '';
    const constraints = q?.constraints?.join('\n- ') || '';
    const visibleTests = q?.visibleTestCases?.map((tc, idx) => 
      `Test ${idx + 1}:\nInput: ${tc.input}\nExpected: ${tc.expectedOutput}`
    ).join('\n\n') || '';

    // Primary current code in Monaco editor
    const currentCode = query.currentEditorCode || query.userCode || '';
    const originalBuggyCode = query.originalBuggyCode || '';
    const codeDiff = query.codeChangesDiff || '';

    // Summarize execution / test runner state
    let executionSummary = '';
    if (query.latestExecutionResult) {
      const er = query.latestExecutionResult;
      executionSummary = `Run Status: ${er.status || 'Executed'}\nPassed Tests: ${er.passedCount ?? 0} / ${er.totalCount ?? 0}\n`;
      if (er.compileOutput && er.compileOutput !== 'Compiled cleanly') {
        executionSummary += `Compiler Output: ${er.compileOutput}\n`;
      }
      if (er.runtimeOutput) {
        executionSummary += `Runtime Output: ${er.runtimeOutput}\n`;
      }
      if (er.testResultsSummary) {
        executionSummary += `Test Breakdown: ${er.testResultsSummary}\n`;
      }
    } else if (query.executionOutput) {
      executionSummary = query.executionOutput;
    } else {
      executionSummary = 'No execution runs recorded yet in this workspace session.';
    }

    let systemInstructions = '';

    if (mode === 'exam' && !isSubmitted) {
      systemInstructions = `You are an expert, strict AI Technical Assessment Proctor and Debugging Mentor for an unsubmitted exam on "${title}".
CRITICAL EXAM MODE SAFETY & CODE TRUTH RULES:
1. The candidate's CURRENT MONACO EDITOR CODE is the absolute source of truth. Always analyze the current code they have in front of them.
2. If the candidate made changes since the original buggy code (see RECENT CODE CHANGES / DIFF), take those changes into account.
3. Do NOT repeat an old diagnosis if the candidate has already fixed that particular line or condition.
4. Under NO circumstances reveal the exact bug, line number of the bug, or bug location.
5. Under NO circumstances provide corrected code, snippets of the fix, or the complete solution.
6. Under NO circumstances solve the problem for the candidate.
7. You MAY explain compiler/runtime errors, algorithmic concepts, invariants, and edge cases.
8. If the current code appears fixed, encourage the candidate to validate against tricky edge cases without spoiling the answer.
9. Format your response strictly as JSON with this schema:
{"message": "guidance text formatted in markdown", "type": "hint"|"error-help"|"review", "revealsSolution": false}`;
    } else if (!isSubmitted) {
      systemInstructions = `You are an expert AI Debugging Mentor helping a developer practice debugging "${title}" in ${lang.toUpperCase()}.
PRACTICE MODE & CODE TRUTH GUIDELINES:
1. The candidate's CURRENT MONACO EDITOR CODE is the absolute source of truth. Always inspect what they currently wrote.
2. If the user changed the code since the original buggy version, analyze the NEW code state. Do NOT repeat an old diagnosis.
3. If the current code appears fixed, confirm that their direction is correct and explain what edge cases or validations to check next.
4. If a new bug was introduced in their modifications, help identify the new issue conceptually.
5. If the latest execution output indicates failures or hasn't been run yet, suggest running tests or analyzing specific failing inputs.
6. Format your response strictly as JSON with this schema:
{"message": "guidance text in markdown", "type": "hint"|"error-help"|"review", "revealsSolution": false}`;
    } else {
      systemInstructions = `You are an expert AI Code Reviewer and DSA Instructor analyzing "${title}" in ${lang.toUpperCase()} AFTER SUBMISSION.
POST-SUBMISSION ANALYSIS:
1. You may provide a full explanation of the bug, why the candidate's final submitted code failed or passed, and the correct optimal approach.
2. Explain relevant edge cases, time complexity, space complexity, and suggest a similar interview problem.
3. Format your response strictly as JSON with this schema:
{"message": "comprehensive explanation in markdown", "type": "explanation", "revealsSolution": true}`;
    }

    let contextBlock = `PROBLEM CONTEXT:
Title: ${title}
Topic: ${topic}
Language: ${lang.toUpperCase()}
Mode: ${mode.toUpperCase()} (Submitted: ${isSubmitted ? 'YES' : 'NO'})

Problem Statement:
${problemStatement}

Constraints:
- ${constraints}

Visible Examples:
${visibleTests}
`;

    if (currentCode) {
      contextBlock += `\n========================================
CURRENT MONACO EDITOR CODE (SOURCE OF TRUTH) [${lang.toUpperCase()}]:
========================================
\`\`\`${lang}
${currentCode}
\`\`\`\n`;
    }

    if (originalBuggyCode && originalBuggyCode !== currentCode) {
      contextBlock += `\n========================================
ORIGINAL BUGGY CODE (INITIAL BENCHMARK):
========================================
\`\`\`${lang}
${originalBuggyCode}
\`\`\`\n`;
    }

    if (codeDiff) {
      contextBlock += `\n========================================
RECENT CODE CHANGES / DIFF FROM INITIAL BUGGY CODE:
========================================
${codeDiff}\n`;
    }

    contextBlock += `\n========================================
LATEST EXECUTION & TEST RUNNER RESULT:
========================================
${executionSummary}\n`;

    const messages: AIMessage[] = [
      { role: 'system', content: systemInstructions },
      { role: 'user', content: `${contextBlock}\nCandidate's Request: ${query.message}` }
    ];

    // Maintain conversation context across turns
    if (query.history && query.history.length > 0) {
      // Include up to last 8 turns (excluding duplicate system prompts)
      const recentTurns = query.history.filter(m => m.role !== 'system').slice(-8);
      messages.splice(1, 0, ...recentTurns);
    }

    return {
      messages,
      questionContext: {
        id: query.questionId,
        title,
        topic,
        language: lang,
        mode,
        isSubmitted
      }
    };
  }

  private validateExamSafety(response: AIChatResponse, isExam: boolean, isSubmitted: boolean): AIChatResponse {
    if (isExam && !isSubmitted) {
      const codeBlockMatches = response.message.match(/```(?:cpp|c|java|python|javascript)?\n([\s\S]*?)```/g);
      if (codeBlockMatches && codeBlockMatches.some(block => block.split('\n').length > 5)) {
        const sanitized = response.message.replace(/```(?:cpp|c|java|python|javascript)?\n([\s\S]*?)```/g, 
          '*(Code block omitted to uphold Exam Mode guidelines. Inspect your algorithm logic conceptually.)*'
        );
        return {
          ...response,
          message: sanitized,
          revealsSolution: false
        };
      }
      return {
        ...response,
        revealsSolution: false
      };
    }

    return response;
  }

  /**
   * Executes AI chat request with automatic fallback:
   * Groq -> Gemini -> Mistral -> Mock
   * Skips unconfigured providers and does not retry failed providers.
   */
  public async handleChat(query: UserAIQuery): Promise<AIChatResponse> {
    const defaultProvider = this.getDefaultProviderName();
    const fallbackOrder = this.getFallbackOrder();
    console.log(`[AIService] AI chat request started. Question: ${query.questionId}, Mode: ${query.mode || 'practice'}`);
    console.log(`[AIService] AI_PROVIDER=${defaultProvider}, Fallback order: [${fallbackOrder.join(', ')}]`);

    const { messages, questionContext } = this.buildPromptMessages(query);

    const chatRequest: AIChatRequest = {
      messages,
      questionContext,
      temperature: query.mode === 'exam' ? 0.2 : 0.3
    };

    // Build ordered list of providers to attempt
    const candidateOrder: string[] = [];
    if (defaultProvider && this.providers.has(defaultProvider)) {
      candidateOrder.push(defaultProvider);
    }
    for (const p of fallbackOrder) {
      if (!candidateOrder.includes(p) && this.providers.has(p)) {
        candidateOrder.push(p);
      }
    }
    if (!candidateOrder.includes('mock') && this.providers.has('mock')) {
      candidateOrder.push('mock');
    }

    const failedProviders: string[] = [];
    const triedProviders: string[] = [];
    const providerErrors: Record<string, string> = {};

    for (const providerName of candidateOrder) {
      if (failedProviders.includes(providerName)) continue;

      const provider = this.providers.get(providerName);
      if (!provider) continue;

      const isConfigured = provider.isConfigured();
      if (!isConfigured) {
        console.log(`[AIService] Provider "${providerName}" is not configured. Skipping.`);
        continue;
      }

      triedProviders.push(providerName);
      console.log(`[AIService] Attempting provider "${providerName}"...`);

      try {
        const response = await provider.chat(chatRequest);
        const validated = this.validateExamSafety(
          response, 
          query.mode === 'exam', 
          Boolean(query.isSubmitted)
        );

        console.log(`[AIService] Provider "${providerName}" succeeded.`);
        return {
          ...validated,
          fallbackChain: triedProviders
        };
      } catch (err: any) {
        failedProviders.push(providerName);
        const safeError = (err.message || 'Unknown error').replace(/Bearer\s+[a-zA-Z0-9_\.-]+/g, 'Bearer [REDACTED]');
        providerErrors[providerName] = safeError;
        console.warn(`[AIService] Provider "${providerName}" failed: ${safeError}. Attempting next configured provider.`);
      }
    }

    // If all configured candidate providers failed, fall back to Mock provider
    console.warn('[AIService] All configured providers failed or were skipped. Falling back to MockAIProvider.');
    const mockProvider = this.providers.get('mock') || new MockAIProvider();
    try {
      const mockResponse = await mockProvider.chat(chatRequest);
      return {
        ...mockResponse,
        fallbackChain: triedProviders.concat(['mock'])
      };
    } catch {
      return {
        message: 'The AI assistant is temporarily unavailable across all providers. Please review the problem statement and compiler output.',
        type: 'error-help',
        revealsSolution: false,
        providerUsed: 'fallback-error',
        fallbackChain: triedProviders
      };
    }
  }
}
