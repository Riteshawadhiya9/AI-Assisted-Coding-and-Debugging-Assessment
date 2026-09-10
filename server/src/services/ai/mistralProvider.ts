import { AIProvider, AIChatRequest, AIChatResponse, AIResponseType } from './aiProvider';

export class MistralProvider implements AIProvider {
  public readonly name = 'mistral';
  private customApiKey?: string;
  private customModel?: string;

  constructor(apiKey?: string, model?: string) {
    this.customApiKey = apiKey;
    this.customModel = model;
  }

  private getApiKey(): string | undefined {
    return this.customApiKey || process.env.MISTRAL_API_KEY;
  }

  private getModel(): string {
    return this.customModel || process.env.MISTRAL_MODEL || 'mistral-small-latest';
  }

  public isConfigured(): boolean {
    const key = this.getApiKey();
    return Boolean(key && key.trim().length > 0);
  }

  public async chat(request: AIChatRequest): Promise<AIChatResponse> {
    const isConfigured = this.isConfigured();
    console.log(`[MistralProvider] MISTRAL_API_KEY configured=${isConfigured}`);

    if (!isConfigured) {
      throw new Error('MistralProvider: MISTRAL_API_KEY is not configured');
    }

    const apiKey = this.getApiKey()!;
    const model = this.getModel();
    console.log(`[MistralProvider] Mistral request started with model=${model}`);

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 12000);

    try {
      const res = await fetch('https://api.mistral.ai/v1/chat/completions', {
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
      console.log(`[MistralProvider] Mistral response status=${res.status}`);

      if (!res.ok) {
        const errorText = await res.text().catch(() => '');
        const safeError = errorText.replace(/Bearer\s+[a-zA-Z0-9_\.-]+/g, 'Bearer [REDACTED]');
        console.warn(`[MistralProvider] Mistral request failed: HTTP ${res.status} - ${safeError}`);

        if (res.status === 429) {
          throw new Error(`MistralProvider rate limit exceeded (HTTP 429): ${safeError}`);
        }
        if (res.status === 401 || res.status === 403) {
          throw new Error(`MistralProvider authentication failure (HTTP ${res.status}): ${safeError}`);
        }
        throw new Error(`MistralProvider request failed with status ${res.status}: ${safeError}`);
      }

      const data = await res.json() as any;
      const content = data?.choices?.[0]?.message?.content;
      if (!content || typeof content !== 'string') {
        throw new Error('MistralProvider returned empty or malformed choice');
      }

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

      return {
        message: messageText,
        type,
        revealsSolution,
        providerUsed: this.name
      };
    } catch (err: any) {
      clearTimeout(timeoutId);
      if (err.name === 'AbortError') {
        console.warn('[MistralProvider] Mistral request timed out after 12 seconds');
        throw new Error('MistralProvider request timed out after 12 seconds');
      }
      throw err;
    }
  }
}
