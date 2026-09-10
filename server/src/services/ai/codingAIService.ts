/**
 * ============================================================================
 * CODING AI SERVICE — STRICT PROMPT & 2,000 TOKEN CONVERSATION BUDGET
 * ============================================================================
 * Features:
 *   - STRICT system prompt for all AI-assisted coding problems
 *   - Hard limit of 2,000 tokens per conversation
 *   - Real-time token tracking (provider exact usage or documented estimation)
 *   - Warning when budget is approaching limit / almost exhausted
 *   - Hard cutoff with: "Conversation token limit reached. Start a new AI conversation to continue."
 *   - Prompt quality evaluation & AI literacy feedback
 * ============================================================================
 */

import { AIProvider, AIChatRequest, AIChatResponse, AIResponseType, AIMessage, estimateTokens } from './aiProvider';
import { GroqProvider } from './groqProvider';
import { GeminiProvider } from './geminiProvider';
import { MistralProvider } from './mistralProvider';
import { MockAIProvider } from './mockAIProvider';
import { codingQuestionRepository } from '../codingQuestionRepository';
import { PromptQualityResult } from '../../types/codingTypes';

export const MAX_CONVERSATION_TOKENS = 2000;

export const STRICT_SYSTEM_PROMPT = `You are a strict AI-assisted coding evaluator and coding assistant.

Your job is to help the candidate understand, reason about, build, review and improve code while evaluating the quality of their interaction with AI.

Never blindly answer vague prompts.

If the user's request is vague, incomplete or lacks necessary context, DO NOT guess and DO NOT generate a generic solution.

Instead, clearly tell the user what information is missing.

For coding requests, consider:
- Problem/goal
- Programming language
- Current code when relevant
- Expected input/output
- Constraints
- Error/output when debugging
- Desired result

Example of a vague prompt:
'Write the code.'

Respond:
'Your prompt is too vague. Specify the programming language, desired approach or requirements, and any constraints. If you already have code, provide it for review.'

Do not reward vague one-line prompts.

When the user provides a good prompt, respond directly and meaningfully.

Always use the latest user-provided/current editor code when reviewing or modifying code.

Never assume the user's code is unchanged.

If the user says they changed code, analyze the CURRENT code supplied with the request.

Do not repeat an old diagnosis when the current code has changed.

For code review, analyze:
- correctness
- logic
- edge cases
- time complexity
- space complexity
- implementation issues

For generated code, encourage the candidate to understand, review, modify and test it.

Do not unnecessarily explain basic concepts unless requested.

Keep responses concise and relevant.

Do not fabricate test results, compiler results or code execution results.

If execution information is unavailable, say so.

The candidate's prompt quality is being evaluated, so prioritize meaningful interaction, reasoning and context over blindly producing code.`;

export interface CodingAIQuery {
  questionId: string;
  message: string;
  currentEditorCode?: string;
  selectedLanguage?: string;
  latestRunResult?: {
    status?: string;
    passedCount?: number;
    totalCount?: number;
    output?: string;
    error?: string;
  };
  mode?: 'practice' | 'assessment';
  history?: AIMessage[];
  action?: 'chat' | 'improve-prompt' | 'review-code' | 'suggest-approach' | 'explain-error';
  currentSessionTokens?: number;
}

export interface CodingAIChatResponse extends AIChatResponse {
  promptQuality?: PromptQualityResult;
  qualityScore?: any;
  tokensUsed?: number;
  tokensRemaining?: number;
  tokenLimitReached?: boolean;
  tokensThisTurn?: number;
  isExact?: boolean;
  estimationMethod?: string;
}

export class CodingAIService {
  private providers: Map<string, AIProvider> = new Map();

  constructor() {
    this.providers.set('groq', new GroqProvider());
    this.providers.set('gemini', new GeminiProvider());
    this.providers.set('mistral', new MistralProvider());
    this.providers.set('mock', new MockAIProvider());
  }

  private getFallbackOrder(): string[] {
    const envOrder = process.env.AI_FALLBACK_ORDER
      ? process.env.AI_FALLBACK_ORDER.split(',').map(s => s.trim().toLowerCase())
      : ['groq', 'gemini', 'mistral'];
    const order = [...envOrder];
    if (!order.includes('mock')) order.push('mock');
    return order;
  }

  private getDefaultProvider(): string {
    return (process.env.AI_PROVIDER || 'groq').toLowerCase();
  }

  public getStatus() {
    return {
      primaryProvider: this.getDefaultProvider(),
      fallbackOrder: this.getFallbackOrder(),
      availableProviders: Array.from(this.providers.entries()).map(([name, p]) => ({
        name,
        configured: p.isConfigured(),
      })),
      tokenBudgetLimit: MAX_CONVERSATION_TOKENS,
    };
  }

  /**
   * Build system + user prompt messages for coding AI.
   */
  private buildPromptMessages(
    query: CodingAIQuery,
    remainingTokens: number
  ): { messages: AIMessage[]; questionContext: AIChatRequest['questionContext'] } {
    const q = codingQuestionRepository.getById(query.questionId, false);
    const lang = (query.selectedLanguage || 'python').toLowerCase();
    const mode = query.mode || 'practice';
    const title = q?.title || 'Coding Problem';
    const topic = q?.topic || 'DSA';
    const problemStatement = q?.problemStatement || q?.description || '';
    const constraints = q?.constraints?.join('\n- ') || 'Standard LeetCode constraints';
    const examples = q?.examples?.map((ex, i) =>
      `Example ${i + 1}:\nInput: ${ex.input}\nOutput: ${ex.output}\n${ex.explanation ? `Explanation: ${ex.explanation}` : ''}`
    ).join('\n\n') || '';

    const currentCode = query.currentEditorCode || '';

    let runSummary = 'No runs executed yet.';
    if (query.latestRunResult) {
      const r = query.latestRunResult;
      runSummary = `Status: ${r.status || 'Executed'}\nPassed: ${r.passedCount ?? 0} / ${r.totalCount ?? 0}`;
      if (r.error) runSummary += `\nError: ${r.error}`;
      if (r.output) runSummary += `\nOutput: ${r.output}`;
    }

    let systemContent = STRICT_SYSTEM_PROMPT;

    // Approaching limit warning injected into system instructions
    if (remainingTokens <= 400) {
      systemContent += `\n\nTOKEN BUDGET ALERT:\nThe candidate has only ${remainingTokens} tokens remaining in their 2,000-token conversation budget. Keep your response extremely brief, focused, and concise. ${
        remainingTokens <= 180
          ? 'Explicitly inform the candidate that their conversation token budget is almost exhausted.'
          : ''
      }`;
    }

    let contextBlock = `PROBLEM CONTEXT:
Problem: ${title} (${topic})
Language: ${lang.toUpperCase()}
Mode: ${mode.toUpperCase()}

Problem Statement:
${problemStatement}

Constraints:
- ${constraints}

Examples:
${examples}
`;

    if (currentCode) {
      contextBlock += `\n========================================
CURRENT EDITOR CODE [${lang.toUpperCase()}]:
========================================
\`\`\`${lang}
${currentCode}
\`\`\`\n`;
    }

    contextBlock += `\n========================================
LATEST RUN EXECUTION RESULT:
========================================
${runSummary}\n`;

    const messages: AIMessage[] = [
      { role: 'system', content: systemContent },
    ];

    // Include recent history
    if (query.history && query.history.length > 0) {
      const recentTurns = query.history.filter(m => m.role !== 'system').slice(-6);
      messages.push(...recentTurns);
    }

    // User's latest prompt with context
    messages.push({
      role: 'user',
      content: `${contextBlock}\nCandidate's Request: ${query.message}`
    });

    return {
      messages,
      questionContext: {
        id: query.questionId,
        title,
        topic,
        language: lang,
        mode: mode as 'practice' | 'exam',
        isSubmitted: false,
      },
    };
  }

  /**
   * Execute AI chat with strict prompt and 2000-token hard limit.
   */
  public async handleChat(query: CodingAIQuery): Promise<CodingAIChatResponse> {
    const currentTokens = Math.max(0, query.currentSessionTokens ?? 0);

    // Hard cutoff: 2,000 token limit
    if (currentTokens >= MAX_CONVERSATION_TOKENS) {
      console.log(`[CodingAIService] Token limit reached (${currentTokens} / ${MAX_CONVERSATION_TOKENS}). Rejecting request.`);
      return {
        message: 'Conversation token limit reached. Start a new AI conversation to continue.',
        type: 'hint',
        revealsSolution: false,
        providerUsed: 'system',
        tokensUsed: MAX_CONVERSATION_TOKENS,
        tokensRemaining: 0,
        tokenLimitReached: true,
        tokensThisTurn: 0,
        isExact: true,
        estimationMethod: 'Conversation token cap enforced',
      };
    }

    const remainingTokens = Math.max(0, MAX_CONVERSATION_TOKENS - currentTokens);

    // If remaining budget is less than enough for minimal turn (~15 tokens)
    if (remainingTokens <= 15) {
      return {
        message: 'Conversation token limit reached. Start a new AI conversation to continue.',
        type: 'hint',
        revealsSolution: false,
        providerUsed: 'system',
        tokensUsed: MAX_CONVERSATION_TOKENS,
        tokensRemaining: 0,
        tokenLimitReached: true,
        tokensThisTurn: 0,
        isExact: true,
        estimationMethod: 'Conversation token cap enforced',
      };
    }

    const defaultProvider = this.getDefaultProvider();
    const fallbackOrder = this.getFallbackOrder();

    console.log(`[CodingAIService] Chat request: question=${query.questionId}, tokensUsed=${currentTokens}, remaining=${remainingTokens}`);

    const { messages, questionContext } = this.buildPromptMessages(query, remainingTokens);

    // Allocate max completion tokens capped by remaining budget
    const maxTokensForResponse = Math.max(30, Math.min(remainingTokens, 450));

    const chatRequest: AIChatRequest = {
      messages,
      questionContext,
      temperature: 0.2,
      maxTokens: maxTokensForResponse,
    };

    // Ordered provider candidates
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

    const triedProviders: string[] = [];

    for (const providerName of candidateOrder) {
      const provider = this.providers.get(providerName);
      if (!provider || !provider.isConfigured()) {
        continue;
      }

      triedProviders.push(providerName);
      console.log(`[CodingAIService] Calling provider "${providerName}" (maxTokens=${maxTokensForResponse})...`);

      try {
        const response = await provider.chat(chatRequest);

        // Determine token usage for this turn
        let turnTokens: number;
        let isExact: boolean;

        if (response.usage && typeof response.usage.totalTokens === 'number' && response.usage.totalTokens > 0) {
          turnTokens = response.usage.totalTokens;
          isExact = response.usage.isExact;
        } else {
          // Documented token estimation: standard ~4 characters per token
          const promptChars = messages.reduce((acc, m) => acc + (m.content?.length || 0), 0);
          const responseChars = (response.message || '').length;
          turnTokens = estimateTokens(`${promptChars + responseChars}`);
          isExact = false;
        }

        const newTokensUsed = Math.min(MAX_CONVERSATION_TOKENS, currentTokens + turnTokens);
        const newTokensRemaining = Math.max(0, MAX_CONVERSATION_TOKENS - newTokensUsed);
        const limitReached = newTokensRemaining <= 0;

        let finalMessage = response.message;
        if (limitReached && !finalMessage.includes('Conversation token limit reached')) {
          finalMessage += '\n\n*(Conversation token limit reached. Start a new AI conversation to continue.)*';
        }

        // Evaluate prompt quality for AI literacy
        let promptQuality: any;
        const pText = (query.message || '').trim();
        if (pText) {
          const isVague = pText.length < 20 || /^(write code|solve|fix it|do it|code)$/i.test(pText);
          const hasContext = Boolean(query.currentEditorCode && query.currentEditorCode.length > 30) || /array|tree|dp|graph|hash|loop|time|space|pointer|index|case|complexity/i.test(pText);
          const isSpecific = pText.length > 25 && /\?|how|why|what|can you|optimize|edge case|explain/i.test(pText);
          const isClear = pText.split(' ').length >= 4;

          const clarity = isVague ? 3 : (isClear ? (pText.length > 60 ? 9 : 8) : 5);
          const context = isVague ? 2 : (hasContext ? 9 : 6);
          const specificity = isVague ? 2 : (isSpecific ? 8 : 5);
          const overall = Math.round((clarity + context + specificity) / 3);

          promptQuality = {
            overall,
            clarity,
            context,
            specificity,
            feedback: isVague
              ? 'Your prompt is too vague. Specify requirements, constraints, or provide code for review.'
              : overall >= 8
              ? 'Excellent prompt! Clear context and specific algorithmic objective.'
              : 'Good question. Mention specific edge cases or complexity goals for a higher AI Literacy score.'
          };
        }

        console.log(`[CodingAIService] Provider "${providerName}" succeeded. Turn tokens: ${turnTokens}, Total: ${newTokensUsed}/${MAX_CONVERSATION_TOKENS}`);

        return {
          message: finalMessage,
          type: response.type,
          revealsSolution: response.revealsSolution,
          providerUsed: providerName,
          fallbackChain: triedProviders,
          promptQuality,
          qualityScore: promptQuality,
          tokensUsed: newTokensUsed,
          tokensRemaining: newTokensRemaining,
          tokenLimitReached: limitReached,
          tokensThisTurn: turnTokens,
          isExact,
          estimationMethod: isExact ? 'Provider actual token count' : 'Estimated (~4 characters per token)'
        };
      } catch (err: any) {
        const safeError = (err.message || 'Unknown error').replace(/Bearer\s+[a-zA-Z0-9_\.-]+/g, 'Bearer [REDACTED]');
        console.warn(`[CodingAIService] Provider "${providerName}" failed: ${safeError}`);
      }
    }

    // Fallback if all providers failed
    console.warn('[CodingAIService] All providers failed. Returning fallback.');
    const estimatedTurn = estimateTokens(query.message + ' Fallback response');
    const newUsed = Math.min(MAX_CONVERSATION_TOKENS, currentTokens + estimatedTurn);
    return {
      message: 'The AI assistant is temporarily unavailable. Please verify your connection or try again shortly.',
      type: 'error-help',
      revealsSolution: false,
      providerUsed: 'fallback-error',
      fallbackChain: triedProviders,
      tokensUsed: newUsed,
      tokensRemaining: Math.max(0, MAX_CONVERSATION_TOKENS - newUsed),
      tokenLimitReached: newUsed >= MAX_CONVERSATION_TOKENS,
      tokensThisTurn: estimatedTurn,
      isExact: false,
      estimationMethod: 'Estimated (~4 characters per token)'
    };
  }
}

export const codingAIService = new CodingAIService();
