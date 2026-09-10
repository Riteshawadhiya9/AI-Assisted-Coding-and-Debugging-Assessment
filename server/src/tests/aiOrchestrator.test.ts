import { AIService } from '../services/ai/aiService';
import { AIProvider, AIChatRequest, AIChatResponse } from '../services/ai/aiProvider';
import { QuestionRepository } from '../services/questionRepository';

class ControllableProvider implements AIProvider {
  public callCount = 0;
  constructor(
    public readonly name: string,
    private configured: boolean,
    private shouldFail: boolean,
    private returnMessage: string = 'Success'
  ) {}

  public isConfigured(): boolean {
    return this.configured;
  }

  public async chat(req: AIChatRequest): Promise<AIChatResponse> {
    this.callCount++;
    if (this.shouldFail) {
      throw new Error(`Simulated failure for provider: ${this.name}`);
    }
    return {
      message: this.returnMessage,
      type: 'hint',
      revealsSolution: false,
      providerUsed: this.name
    };
  }
}

async function runAITestSuite() {
  console.log('=====================================================');
  console.log('🤖 RUNNING PHASE 6 AI ORCHESTRATOR & FALLBACK TESTS');
  console.log('=====================================================\n');

  const questionRepo = new QuestionRepository();
  const sampleQ = questionRepo.getAll(false)[0];
  if (!sampleQ) throw new Error('No questions found in repository to test AI');

  // -------------------------------------------------------------
  // Test 1: Groq works -> response returned immediately
  // -------------------------------------------------------------
  console.log('Test 1: Groq works -> returns Groq response without invoking fallback...');
  {
    const groq = new ControllableProvider('groq', true, false, 'Groq Response');
    const gemini = new ControllableProvider('gemini', true, false, 'Gemini Response');
    const mistral = new ControllableProvider('mistral', true, false, 'Mistral Response');

    const service = new AIService({
      providers: { groq, gemini, mistral },
      defaultProvider: 'groq',
      fallbackOrder: ['groq', 'gemini', 'mistral'],
      questionRepository: questionRepo
    });

    const res = await service.handleChat({
      questionId: sampleQ.id,
      message: 'Help me debug this algorithm'
    });

    if (res.providerUsed !== 'groq' || res.message !== 'Groq Response') {
      throw new Error(`Test 1 Failed: Expected groq response, got ${res.providerUsed}`);
    }
    if (groq.callCount !== 1 || gemini.callCount !== 0 || mistral.callCount !== 0) {
      throw new Error(`Test 1 Failed: Fallback providers were incorrectly invoked: gemini=${gemini.callCount}, mistral=${mistral.callCount}`);
    }
    console.log('  ✔ Passed: Groq succeeded on first attempt; fallbacks remained idle.');
  }

  // -------------------------------------------------------------
  // Test 2: Groq unavailable -> Gemini is attempted
  // -------------------------------------------------------------
  console.log('Test 2: Groq unavailable (fails) -> Gemini is attempted and succeeds...');
  {
    const groq = new ControllableProvider('groq', true, true); // fails
    const gemini = new ControllableProvider('gemini', true, false, 'Gemini Fallback Response');
    const mistral = new ControllableProvider('mistral', true, false);

    const service = new AIService({
      providers: { groq, gemini, mistral },
      defaultProvider: 'groq',
      fallbackOrder: ['groq', 'gemini', 'mistral'],
      questionRepository: questionRepo
    });

    const res = await service.handleChat({
      questionId: sampleQ.id,
      message: 'Help me with edge cases'
    });

    if (res.providerUsed !== 'gemini' || res.message !== 'Gemini Fallback Response') {
      throw new Error(`Test 2 Failed: Expected gemini response, got ${res.providerUsed}`);
    }
    if (groq.callCount !== 1 || gemini.callCount !== 1 || mistral.callCount !== 0) {
      throw new Error(`Test 2 Failed: Incorrect invocation counts: groq=${groq.callCount}, gemini=${gemini.callCount}, mistral=${mistral.callCount}`);
    }
    console.log('  ✔ Passed: Groq failed -> Gemini smoothly handled request.');
  }

  // -------------------------------------------------------------
  // Test 3: Gemini unavailable -> Mistral is attempted
  // -------------------------------------------------------------
  console.log('Test 3: Groq & Gemini unavailable -> Mistral is attempted and succeeds...');
  {
    const groq = new ControllableProvider('groq', true, true); // fails
    const gemini = new ControllableProvider('gemini', true, true); // fails
    const mistral = new ControllableProvider('mistral', true, false, 'Mistral Third Tier');

    const service = new AIService({
      providers: { groq, gemini, mistral },
      defaultProvider: 'groq',
      fallbackOrder: ['groq', 'gemini', 'mistral'],
      questionRepository: questionRepo
    });

    const res = await service.handleChat({
      questionId: sampleQ.id,
      message: 'Explain this error'
    });

    if (res.providerUsed !== 'mistral' || res.message !== 'Mistral Third Tier') {
      throw new Error(`Test 3 Failed: Expected mistral response, got ${res.providerUsed}`);
    }
    if (groq.callCount !== 1 || gemini.callCount !== 1 || mistral.callCount !== 1) {
      throw new Error(`Test 3 Failed: Incorrect call counts`);
    }
    console.log('  ✔ Passed: Groq & Gemini failed -> Mistral handled request.');
  }

  // -------------------------------------------------------------
  // Test 4: All providers unavailable -> Fallback to Mock
  // -------------------------------------------------------------
  console.log('Test 4: All external providers unavailable -> Mock fallback works safely...');
  {
    const groq = new ControllableProvider('groq', true, true);
    const gemini = new ControllableProvider('gemini', true, true);
    const mistral = new ControllableProvider('mistral', true, true);

    const service = new AIService({
      providers: { groq, gemini, mistral },
      defaultProvider: 'groq',
      fallbackOrder: ['groq', 'gemini', 'mistral'],
      questionRepository: questionRepo
    });

    const res = await service.handleChat({
      questionId: sampleQ.id,
      message: 'Why might this test fail?'
    });

    if (!res.message || res.message.length === 0) {
      throw new Error('Test 4 Failed: Expected fallback message from Mock provider');
    }
    console.log(`  ✔ Passed: Handled by provider: ${res.providerUsed} with message length ${res.message.length}`);
  }

  // -------------------------------------------------------------
  // Test 5: Missing provider key -> Provider is skipped
  // -------------------------------------------------------------
  console.log('Test 5: Missing provider key -> Provider is skipped without calling chat()...');
  {
    const groq = new ControllableProvider('groq', false, false); // not configured
    const gemini = new ControllableProvider('gemini', true, false, 'Gemini Skip Test');

    const service = new AIService({
      providers: { groq, gemini },
      defaultProvider: 'groq',
      fallbackOrder: ['groq', 'gemini'],
      questionRepository: questionRepo
    });

    const res = await service.handleChat({
      questionId: sampleQ.id,
      message: 'Give me a hint'
    });

    if (groq.callCount !== 0) {
      throw new Error(`Test 5 Failed: Unconfigured groq provider was called! callCount=${groq.callCount}`);
    }
    if (res.providerUsed !== 'gemini') {
      throw new Error(`Test 5 Failed: Expected gemini to be called after unconfigured groq was skipped`);
    }
    console.log('  ✔ Passed: Unconfigured provider was skipped gracefully.');
  }

  // -------------------------------------------------------------
  // Test 6: Practice Mode receives useful hints
  // -------------------------------------------------------------
  console.log('Test 6: Practice Mode receives useful hints and allows conceptual guidance...');
  {
    const service = new AIService({ questionRepository: questionRepo });
    const res = await service.handleChat({
      questionId: sampleQ.id,
      message: 'Give me a conceptual clue',
      mode: 'practice',
      isSubmitted: false
    });

    if (!res.message || res.type !== 'hint') {
      throw new Error(`Test 6 Failed: Expected hint type, got ${res.type}`);
    }
    console.log('  ✔ Passed: Practice Mode returned valid hint response.');
  }

  // -------------------------------------------------------------
  // Test 7: Exam Mode pre-submission safety guardrails
  // -------------------------------------------------------------
  console.log('Test 7: Exam Mode does not receive the exact solution or code patch before submission...');
  {
    // Simulate an LLM attempting to leak a multi-line code patch
    const leakyProvider: AIProvider = {
      name: 'leaky-llm',
      isConfigured: () => true,
      chat: async () => ({
        message: 'Here is the fixed code:\n```cpp\nint solve() {\n  return 42;\n  int x = 10;\n  int y = 20;\n  return x + y;\n}\n```\nDone.',
        type: 'hint',
        revealsSolution: true,
        providerUsed: 'leaky-llm'
      })
    };

    const service = new AIService({
      providers: { 'leaky-llm': leakyProvider },
      defaultProvider: 'leaky-llm',
      fallbackOrder: ['leaky-llm'],
      questionRepository: questionRepo
    });

    const res = await service.handleChat({
      questionId: sampleQ.id,
      message: 'Give me the correct code to solve this question',
      mode: 'exam',
      isSubmitted: false
    });

    if (res.revealsSolution !== false) {
      throw new Error('Test 7 Failed: revealsSolution must be false in pre-submission Exam Mode');
    }
    if (res.message.includes('int solve()')) {
      throw new Error('Test 7 Failed: Sanitizer failed to redact code solution in unsubmitted exam mode');
    }
    console.log('  ✔ Passed: Exam mode safety sanitizer stripped code solution and protected exam integrity.');
  }

  // -------------------------------------------------------------
  // Test 8: Context verification: Hidden tests & correctCode never sent
  // -------------------------------------------------------------
  console.log('Test 8: Hidden tests and correctCode are never sent in LLM prompt before submission...');
  {
    let capturedPrompt = '';
    const inspectorProvider: AIProvider = {
      name: 'inspector',
      isConfigured: () => true,
      chat: async (req) => {
        capturedPrompt = JSON.stringify(req.messages);
        return {
          message: 'Inspected',
          type: 'hint',
          revealsSolution: false,
          providerUsed: 'inspector'
        };
      }
    };

    const service = new AIService({
      providers: { inspector: inspectorProvider },
      defaultProvider: 'inspector',
      fallbackOrder: ['inspector'],
      questionRepository: questionRepo
    });

    await service.handleChat({
      questionId: sampleQ.id,
      message: 'Review my code',
      mode: 'exam',
      isSubmitted: false,
      userCode: 'int buggy() { return 0; }'
    });

    // Check captured prompt for hidden test cases or correct code
    const rawQ = sampleQ;
    if (rawQ.hiddenTestCases && rawQ.hiddenTestCases.length > 0) {
      for (const htc of rawQ.hiddenTestCases) {
        if (capturedPrompt.includes(htc.input) && htc.input.length > 3) {
          throw new Error(`Test 8 Failed: Hidden test input "${htc.input}" found in AI prompt!`);
        }
      }
    }

    if (rawQ.implementations?.cpp?.correctCode) {
      const correctSnippet = rawQ.implementations.cpp.correctCode.slice(20, 60);
      if (capturedPrompt.includes(correctSnippet)) {
        throw new Error('Test 8 Failed: correctCode found in AI prompt before submission!');
      }
    }

    console.log('  ✔ Passed: Verified zero hidden tests and zero correctCode in pre-submission prompts.');
  }

  // -------------------------------------------------------------
  // Test 9: Status endpoint never exposes API keys
  // -------------------------------------------------------------
  console.log('Test 9: Status report never leaks API keys or secrets...');
  {
    const service = new AIService({ questionRepository: questionRepo });
    const status = service.getStatus();
    const serialized = JSON.stringify(status);

    if (serialized.includes('AI_KEY') || serialized.includes('gsk_') || serialized.includes('AIzaSy')) {
      throw new Error('Test 9 Failed: Found potential API key material in status output');
    }
    if (!status.availableProviders || status.availableProviders.length === 0) {
      throw new Error('Test 9 Failed: Expected provider availability listing');
    }
    console.log('  ✔ Passed: Status metadata is clean and contains no sensitive credentials.');
  }

  console.log('\n=====================================================');
  console.log('✅ ALL PHASE 6 AI ORCHESTRATOR TESTS PASSED SUCCESSFULLY');
  console.log('=====================================================\n');
}

runAITestSuite().catch((err) => {
  console.error('❌ AI Orchestrator Test Suite FAILED:', err);
  process.exit(1);
});
