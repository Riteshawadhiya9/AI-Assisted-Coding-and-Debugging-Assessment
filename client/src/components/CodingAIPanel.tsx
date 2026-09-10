import { useState, useRef, useEffect } from 'react';
import { Send, Sparkles, Bot, User, RefreshCw, Lightbulb, RotateCcw, AlertTriangle } from 'lucide-react';
import type { CodingAIChatMessage, CodingQuestion, CodingLanguage } from '../types';

const TOTAL_TOKEN_BUDGET = 2000;

interface CodingAIPanelProps {
  question: CodingQuestion;
  language: CodingLanguage;
  currentCode: string;
  mode: 'practice' | 'assessment';
}

export default function CodingAIPanel({
  question,
  language,
  currentCode,
  mode
}: CodingAIPanelProps) {
  const [messages, setChatMessages] = useState<CodingAIChatMessage[]>([
    {
      id: 'welcome',
      role: 'assistant',
      content: mode === 'assessment'
        ? `🛡️ **AI-Assisted Assessment Mode Active.**\n\nI am your strict AI coding evaluator for **${question.number ? `${question.number}. ` : ''}${question.title}**.\n\n*Assessment Guidelines:*\n- Your prompt clarity, context, and specificity are strictly evaluated.\n- Vague prompts (e.g. "Write the code") will be rejected with requests for missing specifications.\n- You have a **2,000-token conversation budget** for this problem.`
        : `👋 **AI-Assisted Coding Practice Session.**\n\nI am here to help you reason about, build, review, and test your code for **${question.number ? `${question.number}. ` : ''}${question.title}**.\n\n*Guidelines:*\n- State your approach, programming language, and requirements clearly.\n- 2,000-token budget allocated for this conversation.`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }
  ]);

  const [inputPrompt, setInputPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [tokensUsed, setTokensUsed] = useState<number>(0);
  const [isExactCount, setIsExactCount] = useState<boolean>(true);
  const [tokenLimitReached, setTokenLimitReached] = useState<boolean>(false);
  const [lastQualityScore, setLastQualityScore] = useState<{
    overall: number;
    clarity: number;
    context: number;
    specificity: number;
    feedback: string;
  } | null>(null);

  // Dedicated ref to scroll ONLY the internal message container
  const messagesContainerRef = useRef<HTMLDivElement>(null);

  const tokensRemaining = Math.max(0, TOTAL_TOKEN_BUDGET - tokensUsed);

  // Internal scroll only: never scrolls the window or parent layout
  const scrollToBottom = () => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop = messagesContainerRef.current.scrollHeight;
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleStartNewConversation = () => {
    setChatMessages([
      {
        id: `welcome-${Date.now()}`,
        role: 'assistant',
        content: `🔄 **New Conversation Started.**\n\nFresh 2,000-token conversation budget initialized for **${question.number ? `${question.number}. ` : ''}${question.title}**.\n\nAsk a well-specified question or request code review with your current ${language.toUpperCase()} implementation.`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }
    ]);
    setTokensUsed(0);
    setIsExactCount(true);
    setTokenLimitReached(false);
    setLastQualityScore(null);
    setInputPrompt('');
  };

  const handleSendMessage = async (customPrompt?: string) => {
    const promptToSend = (customPrompt || inputPrompt).trim();
    if (!promptToSend || isLoading) return;

    // Hard cutoff check
    if (tokensRemaining <= 0 || tokenLimitReached) {
      alert('Conversation token limit reached. Start a new AI conversation to continue.');
      return;
    }

    const userMessage: CodingAIChatMessage = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: promptToSend,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setChatMessages(prev => [...prev, userMessage]);
    if (!customPrompt) setInputPrompt('');
    setIsLoading(true);

    // Initial prompt token estimation for immediate UI update
    const estimatedPromptTokens = Math.max(1, Math.ceil(promptToSend.length / 4));
    const optimisticTokensUsed = Math.min(TOTAL_TOKEN_BUDGET, tokensUsed + estimatedPromptTokens);
    setTokensUsed(optimisticTokensUsed);

    try {
      const response = await fetch('/api/coding/ai/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          questionId: question.id,
          message: promptToSend,
          prompt: promptToSend,
          currentEditorCode: currentCode,
          selectedLanguage: language,
          mode,
          history: messages.map(m => ({ role: m.role, content: m.content })),
          currentSessionTokens: tokensUsed,
          tokensUsed: tokensUsed
        })
      });

      if (!response.ok) {
        throw new Error(`AI service responded with HTTP ${response.status}`);
      }

      const data = await response.json();

      const assistantMessage: CodingAIChatMessage = {
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: data.message || data.reply || data.text || 'I processed your request.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        qualityScore: data.qualityScore || data.promptQuality
      };

      // Update token tracking metrics from server
      if (typeof data.tokensUsed === 'number') {
        setTokensUsed(data.tokensUsed);
      }
      if (typeof data.isExact === 'boolean') {
        setIsExactCount(data.isExact);
      }
      if (data.tokenLimitReached || (data.tokensRemaining !== undefined && data.tokensRemaining <= 0)) {
        setTokenLimitReached(true);
      }

      if (data.qualityScore || data.promptQuality) {
        setLastQualityScore(data.qualityScore || data.promptQuality);
      }

      setChatMessages(prev => [...prev, assistantMessage]);
    } catch (err: any) {
      setChatMessages(prev => [
        ...prev,
        {
          id: `err-${Date.now()}`,
          role: 'assistant',
          content: `⚠️ Could not reach AI service: ${err.message || 'Check server connection.'}`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const quickPrompts = [
    'Can you explain the intuition behind this problem without giving the full code?',
    'What are the critical edge cases to consider for this data structure?',
    'Review my current code for potential bugs or suboptimal time complexity.',
    'Give me a hint on how to optimize space complexity.'
  ];

  return (
    <div className="flex flex-col h-full overflow-hidden bg-[#0d1322] border-l border-slate-800/80">
      {/* Fixed Header Bar */}
      <div className="p-3 border-b border-slate-800 bg-[#0f172a]/80 flex items-center justify-between shrink-0">
        <div className="flex items-center gap-2">
          <div className="size-7 rounded-md bg-indigo-500/20 text-indigo-400 grid place-items-center border border-indigo-500/30">
            <Sparkles className="size-4" />
          </div>
          <div>
            <div className="text-xs font-bold text-white flex items-center gap-1.5">
              <span>AI Coding Assistant</span>
              <span className="text-[10px] px-1.5 py-0.2 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 uppercase font-semibold">
                Strict Evaluator
              </span>
            </div>
            <div className="text-[11px] text-slate-400">
              {mode === 'assessment' ? 'Proctored Assessment Session' : 'Strict Practice Mentor'}
            </div>
          </div>
        </div>

        {lastQualityScore && (
          <div className="flex items-center gap-2 bg-slate-800/60 px-2.5 py-1 rounded-md border border-slate-700/50">
            <span className="text-[10px] text-slate-400 uppercase font-bold tracking-wider">Prompt Quality:</span>
            <span className={`text-xs font-bold ${
              lastQualityScore.overall >= 8 ? 'text-emerald-400' :
              lastQualityScore.overall >= 5 ? 'text-amber-400' : 'text-rose-400'
            }`}>
              {lastQualityScore.overall}/10
            </span>
          </div>
        )}
      </div>

      {/* Fixed Prompt Quality Banner */}
      {lastQualityScore && (
        <div className="px-3 py-1.5 bg-indigo-950/30 border-b border-indigo-900/40 text-[11px] text-indigo-300 flex items-center justify-between shrink-0">
          <span className="truncate">💡 <strong>Feedback:</strong> {lastQualityScore.feedback}</span>
          <div className="flex gap-2 text-[10px] shrink-0 ml-2">
            <span>Clarity: <strong className="text-indigo-200">{lastQualityScore.clarity}/10</strong></span>
            <span>Context: <strong className="text-indigo-200">{lastQualityScore.context}/10</strong></span>
            <span>Specificity: <strong className="text-indigo-200">{lastQualityScore.specificity}/10</strong></span>
          </div>
        </div>
      )}

      {/* Token Warning Banner when budget is low */}
      {tokensRemaining > 0 && tokensRemaining <= 350 && (
        <div className="px-3 py-1.5 bg-amber-950/40 border-b border-amber-800/50 text-[11px] text-amber-300 flex items-center gap-1.5 shrink-0">
          <AlertTriangle className="size-3.5 text-amber-400 shrink-0" />
          <span>Conversation token budget is almost exhausted ({tokensRemaining.toLocaleString()} tokens left). Keep prompts concise.</span>
        </div>
      )}

      {/* Scrollable Messages Area: scrolls ONLY internally */}
      <div
        ref={messagesContainerRef}
        className="flex-1 min-h-0 overflow-y-auto p-4 space-y-4 select-text"
      >
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`flex gap-3 ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            {msg.role !== 'user' && (
              <div className="size-7 rounded-md bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 grid place-items-center shrink-0 mt-0.5">
                <Bot className="size-4" />
              </div>
            )}

            <div
              className={`max-w-[85%] rounded-lg px-3.5 py-2.5 text-xs leading-relaxed ${
                msg.role === 'user'
                  ? 'bg-indigo-600 text-white shadow-md'
                  : 'bg-slate-900/90 border border-slate-800 text-slate-200'
              }`}
            >
              <div className="whitespace-pre-wrap font-sans">{msg.content}</div>
              <div className={`text-[10px] mt-1.5 text-right ${
                msg.role === 'user' ? 'text-indigo-200' : 'text-slate-500'
              }`}>
                {msg.timestamp}
              </div>
            </div>

            {msg.role === 'user' && (
              <div className="size-7 rounded-md bg-slate-700 text-slate-300 grid place-items-center shrink-0 mt-0.5">
                <User className="size-4" />
              </div>
            )}
          </div>
        ))}

        {isLoading && (
          <div className="flex gap-3 items-center text-xs text-slate-400 py-2">
            <div className="size-7 rounded-md bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 grid place-items-center">
              <RefreshCw className="size-3.5 animate-spin" />
            </div>
            <span>Evaluating code context and formulating response...</span>
          </div>
        )}
      </div>

      {/* Fixed Suggested Prompts Bar */}
      {tokensRemaining > 0 && !tokenLimitReached && (
        <div className="px-3 py-2 border-t border-slate-800/80 bg-slate-950/40 shrink-0">
          <div className="text-[10px] font-semibold uppercase tracking-wider text-slate-500 mb-1.5 flex items-center gap-1">
            <Lightbulb className="size-3 text-amber-400" />
            <span>Suggested Prompts</span>
          </div>
          <div className="flex flex-wrap gap-1.5">
            {quickPrompts.map((prompt, idx) => (
              <button
                key={idx}
                disabled={isLoading}
                onClick={() => handleSendMessage(prompt)}
                className="text-[11px] text-left text-slate-300 bg-slate-900/80 hover:bg-slate-800 hover:text-white border border-slate-800 px-2 py-1 rounded transition-colors disabled:opacity-50"
              >
                {prompt}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Fixed Chat Input Area */}
      <div className="p-3 border-t border-slate-800 bg-[#0c1220] shrink-0">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSendMessage();
          }}
          className="flex items-center gap-2"
        >
          <input
            type="text"
            value={inputPrompt}
            onChange={(e) => setInputPrompt(e.target.value)}
            disabled={isLoading || tokensRemaining <= 0 || tokenLimitReached}
            placeholder={
              tokensRemaining <= 0 || tokenLimitReached
                ? 'Conversation token limit reached. Start a new AI conversation to continue.'
                : "Ask the AI assistant (e.g., 'Analyze edge cases in my current solution')..."
            }
            className="flex-1 bg-slate-900 border border-slate-700/80 rounded-lg px-3 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500 disabled:opacity-50"
          />
          <button
            type="submit"
            disabled={!inputPrompt.trim() || isLoading || tokensRemaining <= 0 || tokenLimitReached}
            className="size-8 rounded-lg bg-indigo-600 hover:bg-indigo-500 disabled:opacity-40 text-white grid place-items-center transition-colors shrink-0"
          >
            <Send className="size-4" />
          </button>
        </form>
      </div>

      {/* Fixed Token Counter Status Bar */}
      <div className="h-8 px-3 shrink-0 bg-slate-950 border-t border-slate-800/80 flex items-center justify-between text-xs select-none">
        <div className="flex items-center gap-2">
          <span className={`size-2 rounded-full shrink-0 ${
            tokensRemaining <= 0 || tokenLimitReached ? 'bg-rose-500' :
            tokensRemaining <= 350 ? 'bg-amber-400 animate-pulse' :
            'bg-emerald-400'
          }`} />
          <span className={`font-mono text-[11px] font-medium ${
            tokensRemaining <= 0 || tokenLimitReached ? 'text-rose-400 font-bold' :
            tokensRemaining <= 350 ? 'text-amber-300 font-semibold' :
            'text-slate-300'
          }`}>
            {tokensRemaining.toLocaleString()} / 2,000 tokens remaining
          </span>
          {!isExactCount && (
            <span className="text-[10px] text-slate-500 font-sans" title="Estimated at standard ~4 characters per token">
              (estimated)
            </span>
          )}
        </div>

        <button
          type="button"
          onClick={handleStartNewConversation}
          className="inline-flex items-center gap-1 text-[11px] font-semibold text-indigo-400 hover:text-indigo-300 px-2 py-0.5 rounded hover:bg-slate-800/60 transition-colors"
          title="Start a new conversation with a fresh 2,000-token budget"
        >
          <RotateCcw className="size-3" />
          <span>New Conversation</span>
        </button>
      </div>
    </div>
  );
}
