export type AIMessageRole = 'system' | 'user' | 'assistant';

export interface AIMessage {
  role: AIMessageRole;
  content: string;
}

export type AIResponseType = 'hint' | 'explanation' | 'review' | 'error-help';

export interface AIChatRequest {
  messages: AIMessage[];
  temperature?: number;
  maxTokens?: number;
  questionContext?: {
    id: string;
    title: string;
    topic: string;
    language: string;
    mode: 'practice' | 'exam';
    isSubmitted: boolean;
  };
}

export interface AIUsageMetrics {
  promptTokens: number;
  completionTokens: number;
  totalTokens: number;
  isExact: boolean;
}

export function estimateTokens(text: string): number {
  if (!text) return 0;
  // Standard token estimation heuristic: ~4 characters per token for typical code and English text
  return Math.max(1, Math.ceil(text.length / 4));
}

export interface AIChatResponse {
  message: string;
  type: AIResponseType;
  revealsSolution: boolean;
  providerUsed: string;
  fallbackChain?: string[];
  usage?: AIUsageMetrics;
}

export interface AIProvider {
  readonly name: string;
  isConfigured(): boolean;
  chat(request: AIChatRequest): Promise<AIChatResponse>;
}

