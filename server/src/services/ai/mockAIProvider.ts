import { AIProvider, AIChatRequest, AIChatResponse, AIResponseType } from './aiProvider';

export class MockAIProvider implements AIProvider {
  public readonly name = 'mock';

  public isConfigured(): boolean {
    return true; // Mock provider is always available as the ultimate fallback
  }

  public async chat(request: AIChatRequest): Promise<AIChatResponse> {
    const userMsgRaw = [...request.messages].reverse().find(m => m.role === 'user')?.content || '';
    const requestMatch = userMsgRaw.match(/(?:candidate's request|user request):\s*([\s\S]*)$/i);
    const lastUserMessage = (requestMatch ? requestMatch[1] : userMsgRaw).toLowerCase().trim();
    const ctx = request.questionContext;
    const isExam = ctx?.mode === 'exam';
    const isSubmitted = ctx?.isSubmitted ?? false;
    const lang = ctx?.language || 'code';
    const topic = ctx?.topic || 'DSA';

    // Guard in exam mode before submission
    if (isExam && !isSubmitted) {
      if (lastUserMessage.includes('solution') || lastUserMessage.includes('correct code') || lastUserMessage.includes('give me code') || lastUserMessage.includes('fix')) {
        return {
          message: `[Exam Mode Restricted] Under assessment conditions, full solutions or direct code patches cannot be provided before submission.\n\nGuidance: Consider tracing your logic with a small input. Check your base condition, loop boundaries, and state transitions in ${lang.toUpperCase()}.`,
          type: 'hint',
          revealsSolution: false,
          providerUsed: this.name
        };
      }
    }

    // Determine type of response
    let responseType: AIResponseType = 'hint';
    let message = '';

    if (lastUserMessage.includes('error') || lastUserMessage.includes('compil') || lastUserMessage.includes('segfault') || lastUserMessage.includes('exception')) {
      responseType = 'error-help';
      message = `### Error Analysis (${lang.toUpperCase()})\n\n1. **Likely Cause:** Memory access out of bounds, uninitialized pointer/variable, or off-by-one loop indexing.\n2. **Actionable Check:** Verify where arrays or dynamic containers are accessed. Ensure base cases terminate recursive calls before dereferencing invalid nodes.`;
    } else if (lastUserMessage.includes('review') || lastUserMessage.includes('approach')) {
      responseType = 'review';
      message = `### Approach Review (${topic})\n\n- **Algorithm Invariant:** Your general approach targets the right problem space for ${topic}.\n- **Critical State:** Check whether visited states or memoized subproblems are updated before returning.\n- **Complexity:** Ensure your approach meets the expected time and space bounds without redundant iterations.`;
    } else if (lastUserMessage.includes('why might this test fail') || lastUserMessage.includes('test fail')) {
      responseType = 'hint';
      message = `### Test Failure Clue\n\n- Pay attention to boundary inputs: empty structures, single-element collections, or disconnected components.\n- Check if values accumulate correctly across recursive frames rather than getting overwritten.`;
    } else if (isSubmitted) {
      responseType = 'explanation';
      message = `### Post-Submission Solution Analysis\n\n1. **Core Problem:** The algorithm needed careful synchronization between state transitions and boundary termination.\n2. **Correction:** Ensure base cases return neutral elements and transitions strictly handle cycle prevention or memoization.\n3. **Complexity:** An optimal solution runs within standard optimal bounds for ${topic} with minimal auxiliary space.`;
    } else {
      // Default hint
      responseType = 'hint';
      message = `### Conceptual Hint\n\n- Carefully inspect the initialization values and boundary conditions for this ${topic} problem.\n- Trace the flow with a minimal example (e.g., size 0, 1, or 2) to see where the actual runtime behavior diverges from expected logic.`;
    }

    const totalChars = request.messages.reduce((sum, m) => sum + (m.content?.length || 0), 0) + message.length;
    const estimatedTotal = Math.max(1, Math.ceil(totalChars / 4));
    const estimatedCompletion = Math.max(1, Math.ceil(message.length / 4));

    return {
      message,
      type: responseType,
      revealsSolution: false,
      providerUsed: this.name,
      usage: {
        promptTokens: Math.max(1, estimatedTotal - estimatedCompletion),
        completionTokens: estimatedCompletion,
        totalTokens: estimatedTotal,
        isExact: false
      }
    };
  }
}
