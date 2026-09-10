import { AIProvider, AIChatRequest, AIChatResponse, AIResponseType } from './aiProvider';

export class GroqProvider implements AIProvider {
  public readonly name = 'groq';
  private customApiKey?: string;
  private customModel?: string;

  constructor(apiKey?: string, model?: string) {
    this.customApiKey = apiKey;
    this.customModel = model;
  }

  private getApiKey(): string | undefined {
    return this.customApiKey || process.env.GROQ_API_KEY;
  }

  private getModel(): string {
    return this.customModel || process.env.GROQ_MODEL || 'qwen/qwen3.8-27b';
  }

  public isConfigured(): boolean {
    const key = this.getApiKey();
    return Boolean(key && key.trim().length > 0);
  }

  public async chat(request: AIChatRequest): Promise<AIChatResponse> {
    const isConfigured = this.isConfigured();
    console.log(`[GroqProvider] GROQ_API_KEY configured=${isConfigured}`);

    if (!isConfigured) {
      throw new Error('GroqProvider: GROQ_API_KEY is not configured');
    }

    const apiKey = this.getApiKey()!;
    const model = this.getModel();
    console.log(`[GroqProvider] Groq request started with model=${model}`);

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 12000); // 12s timeout

    try {
      const res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
          model,
          messages: request.messages,
          temperature: request.temperature ?? 0.3,
          max_tokens: request.maxTokens ?? 1024
        }),
        signal: controller.signal
      });

      clearTimeout(timeoutId);
      console.log(`[GroqProvider] Groq response status=${res.status}`);

      if (!res.ok) {
        const errorText = await res.text().catch(() => '');
        const safeError = errorText.replace(/gsk_[a-zA-Z0-9_-]+/g, '[REDACTED]');
        console.warn(`[GroqProvider] Groq request failed: HTTP ${res.status} - ${safeError}`);

        if (res.status === 429) {
          throw new Error(`GroqProvider rate limit exceeded (HTTP 429): ${safeError}`);
        }
        if (res.status === 401 || res.status === 403) {
          throw new Error(`GroqProvider authentication failure (HTTP ${res.status}): ${safeError}`);
        }
        throw new Error(`GroqProvider request failed with status ${res.status}: ${safeError}`);
      }

      const data = await res.json() as any;
      const content = data?.choices?.[0]?.message?.content;
      if (!content || typeof content !== 'string') {
        throw new Error('GroqProvider returned empty or malformed choice');
      }

      // Try parsing structured JSON response if returned by model
      let type: AIResponseType = 'hint';
      let messageText = content;
      let revealsSolution = false;

      try {
        const jsonMatch = content.match(/\{[\s\S]*\}/);
        if (jsonMatch) {
          const parsed = JSON.parse(jsonMatch[0]);
          if (parsed.message) messageText = parsed.message;
          if (parsed.type) type = parsed.type;
          if (typeof parsed.revealsSolution === 'boolean') revealsSolution = parsed.revealsSolution;
        }
      } catch {
        // Fall back to plain text content
      }

      const usage = data?.usage ? {
        promptTokens: data.usage.prompt_tokens ?? 0,
        completionTokens: data.usage.completion_tokens ?? 0,
        totalTokens: data.usage.total_tokens ?? 0,
        isExact: true
      } : undefined;

      return {
        message: messageText,
        type,
        revealsSolution,
        providerUsed: this.name,
        usage
      };
    } catch (err: any) {
      clearTimeout(timeoutId);
      if (err.name === 'AbortError') {
        console.warn('[GroqProvider] Groq request timed out after 12 seconds');
        throw new Error('GroqProvider request timed out after 12 seconds');
      }
      throw err;
    }
  }
}
