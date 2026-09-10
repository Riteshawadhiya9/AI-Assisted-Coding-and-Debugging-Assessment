import { AIProvider, AIChatRequest, AIChatResponse, AIResponseType } from './aiProvider';

export class GeminiProvider implements AIProvider {
  public readonly name = 'gemini';
  private customApiKey?: string;
  private customModel?: string;

  constructor(apiKey?: string, model?: string) {
    this.customApiKey = apiKey;
    this.customModel = model;
  }

  private getApiKey(): string | undefined {
    return this.customApiKey || process.env.GEMINI_API_KEY;
  }

  private getModel(): string {
    return this.customModel || process.env.GEMINI_MODEL || 'gemini-2.5-flash';
  }

  public isConfigured(): boolean {
    const key = this.getApiKey();
    return Boolean(key && key.trim().length > 0);
  }

  public async chat(request: AIChatRequest): Promise<AIChatResponse> {
    const isConfigured = this.isConfigured();
    console.log(`[GeminiProvider] GEMINI_API_KEY configured=${isConfigured}`);

    if (!isConfigured) {
      throw new Error('GeminiProvider: GEMINI_API_KEY is not configured');
    }

    const apiKey = this.getApiKey()!;
    const model = this.getModel();
    console.log(`[GeminiProvider] Gemini request started with model=${model}`);

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 12000);

    try {
      // Separate system messages from user/model messages
      const systemMessages = request.messages.filter(m => m.role === 'system');
      const nonSystemMessages = request.messages.filter(m => m.role !== 'system');

      const systemPrompt = systemMessages.map(m => m.content).join('\n\n');

      const contents = nonSystemMessages.map(m => ({
        role: m.role === 'assistant' ? 'model' : 'user',
        parts: [{ text: m.content }]
      }));

      if (contents.length === 0) {
        contents.push({ role: 'user', parts: [{ text: 'Hello' }] });
      }

      const bodyPayload: any = {
        contents,
        generationConfig: {
          temperature: request.temperature ?? 0.3,
          maxOutputTokens: request.maxTokens ?? 1024
        }
      };

      if (systemPrompt) {
        bodyPayload.systemInstruction = {
          parts: [{ text: systemPrompt }]
        };
      }

      const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(bodyPayload),
        signal: controller.signal
      });

      clearTimeout(timeoutId);
      console.log(`[GeminiProvider] Gemini response status=${res.status}`);

      if (!res.ok) {
        const errText = await res.text().catch(() => '');
        const safeError = errText.replace(/key=[a-zA-Z0-9_\.-]+/g, 'key=[REDACTED]');
        console.warn(`[GeminiProvider] Gemini request failed: HTTP ${res.status} - ${safeError}`);

        if (res.status === 429) {
          throw new Error(`GeminiProvider quota or rate limit exceeded (HTTP 429): ${safeError}`);
        }
        if (res.status === 400 || res.status === 403) {
          throw new Error(`GeminiProvider authentication failure (HTTP ${res.status}): ${safeError}`);
        }
        throw new Error(`GeminiProvider request failed with status ${res.status}: ${safeError}`);
      }

      const data = await res.json() as any;
      const candidateText = data?.candidates?.[0]?.content?.parts?.[0]?.text;

      if (!candidateText || typeof candidateText !== 'string') {
        throw new Error('GeminiProvider returned empty or malformed candidate text');
      }

      let type: AIResponseType = 'hint';
      let messageText = candidateText;
      let revealsSolution = false;

      try {
        const jsonMatch = candidateText.match(/\{[\s\S]*\}/);
        if (jsonMatch) {
          const parsed = JSON.parse(jsonMatch[0]);
          if (parsed.message) messageText = parsed.message;
          if (parsed.type) type = parsed.type;
          if (typeof parsed.revealsSolution === 'boolean') revealsSolution = parsed.revealsSolution;
        }
      } catch {
        // Fall back to plain text content
      }

      const usage = data?.usageMetadata ? {
        promptTokens: data.usageMetadata.promptTokenCount ?? 0,
        completionTokens: data.usageMetadata.candidatesTokenCount ?? 0,
        totalTokens: data.usageMetadata.totalTokenCount ?? 0,
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
        console.warn('[GeminiProvider] Gemini request timed out after 12 seconds');
        throw new Error('GeminiProvider request timed out after 12 seconds');
      }
      throw err;
    }
  }
}
