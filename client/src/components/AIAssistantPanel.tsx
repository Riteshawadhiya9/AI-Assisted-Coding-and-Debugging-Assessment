import { useState, useEffect, useRef } from 'react';
import { 
  Send, Sparkles, Bot, AlertTriangle, ShieldCheck, 
  RotateCcw, HelpCircle, Code2, CheckCircle2, ChevronRight, FileCode
} from 'lucide-react';
import type { Question, Language } from '../types';

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  type?: 'hint' | 'explanation' | 'review' | 'error-help';
  providerUsed?: string;
  timestamp: string;
}

export interface AIAssistantPanelProps {
  question: Question;
  selectedLanguage: Language;
  currentEditorCode: string;
  originalBuggyCode: string;
  lastRunCode: string;
  lastSubmittedCode?: string;
  codeChangesDiff: string;
  latestExecutionResult: any;
  consoleLogs: string;
  sessionMode: 'practice' | 'exam';
  isSubmitted: boolean;
  messages: ChatMessage[];
  onUpdateMessages: (msgs: ChatMessage[]) => void;
}

export default function AIAssistantPanel({
  question,
  selectedLanguage,
  currentEditorCode,
  originalBuggyCode,
  lastRunCode,
  lastSubmittedCode,
  codeChangesDiff,
  latestExecutionResult,
  consoleLogs,
  sessionMode,
  isSubmitted,
  messages,
  onUpdateMessages
}: AIAssistantPanelProps) {
  const [inputMessage, setInputMessage] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll on new message
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const hasCodeChanges = Boolean(codeChangesDiff && !codeChangesDiff.includes('No modifications'));

  const handleSendMessage = async (textToSend?: string, promptType?: 'hint' | 'explanation' | 'review' | 'error-help') => {
    const text = (textToSend || inputMessage).trim();
    if (!text || loading) return;

    const userMsg: ChatMessage = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: text,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    const newHistory = [...messages, userMsg];
    onUpdateMessages(newHistory);
    if (!textToSend) setInputMessage('');
    setLoading(true);

    try {
      const res = await fetch('/api/ai/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          questionId: question.id,
          message: text,
          currentEditorCode,
          originalBuggyCode,
          lastRunCode,
          lastSubmittedCode,
          codeChangesDiff,
          latestExecutionResult,
          userCode: currentEditorCode,
          executionOutput: consoleLogs,
          language: selectedLanguage,
          mode: sessionMode,
          isSubmitted,
          type: promptType,
          history: newHistory.slice(-8).map(m => ({ role: m.role, content: m.content }))
        })
      });

      if (!res.ok) {
        throw new Error(`AI Request returned status ${res.status}`);
      }

      const data = await res.json();

      const aiMsg: ChatMessage = {
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: data.message || 'No response generated.',
        type: data.type || 'hint',
        providerUsed: data.providerUsed,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };

      onUpdateMessages([...newHistory, aiMsg]);
    } catch (err: any) {
      const errorMsg: ChatMessage = {
        id: `error-${Date.now()}`,
        role: 'assistant',
        content: `⚠️ The AI service encountered a temporary issue. Local debugging check: Examine boundary conditions, pointer/null checks, and base cases in your current ${selectedLanguage.toUpperCase()} code.`,
        type: 'error-help',
        providerUsed: 'fallback-error',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      onUpdateMessages([...newHistory, errorMsg]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    onUpdateMessages([
      {
        id: `reset-${Date.now()}`,
        role: 'assistant',
        content: `Conversation reset. Analyzing your current ${selectedLanguage.toUpperCase()} code in the Monaco editor. How can I help you debug this problem?`,
        type: 'hint',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }
    ]);
  };

  return (
    <div className="flex flex-col h-full overflow-hidden bg-[#090d16] text-xs">
      {/* Header bar */}
      <div className="px-3.5 py-2.5 bg-[#0e1626] border-b border-slate-800 flex items-center justify-between shrink-0">
        <div className="flex items-center gap-2">
          <div className="size-6 rounded-md bg-indigo-600/20 border border-indigo-500/40 flex items-center justify-center text-indigo-400">
            <Bot className="size-3.5" />
          </div>
          <div>
            <div className="font-bold text-white flex items-center gap-1.5 leading-none">
              <span>AI Debug Assistant</span>
              <span className="size-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            </div>
            <div className="flex items-center gap-1.5 mt-0.5">
              <span className="text-[10px] text-slate-400 flex items-center gap-1">
                <FileCode className="size-2.5 text-indigo-400" /> Current Monaco Code Active
              </span>
              {hasCodeChanges && (
                <span className="text-[9px] text-emerald-400 bg-emerald-950/40 border border-emerald-900/40 px-1 rounded">
                  Modified
                </span>
              )}
            </div>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {sessionMode === 'exam' && !isSubmitted ? (
            <span className="flex items-center gap-1 text-[10px] font-bold text-amber-400 bg-amber-950/40 border border-amber-500/30 px-2 py-0.5 rounded-full">
              <ShieldCheck className="size-3" /> Exam Guarded
            </span>
          ) : (
            <span className="flex items-center gap-1 text-[10px] font-bold text-indigo-400 bg-indigo-950/40 border border-indigo-500/30 px-2 py-0.5 rounded-full">
              <Sparkles className="size-3" /> {isSubmitted ? 'Post-Submit' : 'Practice'}
            </span>
          )}

          <button
            onClick={clearChat}
            className="p-1 text-slate-500 hover:text-slate-300 hover:bg-slate-800 rounded transition-all cursor-pointer"
            title="Clear Conversation History"
          >
            <RotateCcw className="size-3" />
          </button>
        </div>
      </div>

      {/* Quick Action Chips */}
      <div className="px-3 py-2 bg-[#0a0f1d] border-b border-slate-800/80 flex items-center gap-1.5 overflow-x-auto shrink-0 scrollbar-thin">
        {!isSubmitted ? (
          <>
            <button
              onClick={() => handleSendMessage('Give me a hint based on my current code and test results.', 'hint')}
              disabled={loading}
              className="whitespace-nowrap px-2.5 py-1 rounded-md bg-slate-900 border border-indigo-500/30 hover:border-indigo-500 text-indigo-300 font-semibold text-[11px] transition-all flex items-center gap-1 cursor-pointer disabled:opacity-50"
            >
              <Sparkles className="size-3 text-indigo-400" /> Give Hint
            </button>
            <button
              onClick={() => handleSendMessage('Can you explain the latest test runner / compiler errors in my code?', 'error-help')}
              disabled={loading}
              className="whitespace-nowrap px-2.5 py-1 rounded-md bg-slate-900 border border-rose-500/30 hover:border-rose-500 text-rose-300 font-semibold text-[11px] transition-all flex items-center gap-1 cursor-pointer disabled:opacity-50"
            >
              <AlertTriangle className="size-3 text-rose-400" /> Explain Error
            </button>
            <button
              onClick={() => handleSendMessage('Review my current code changes and algorithmic approach.', 'review')}
              disabled={loading}
              className="whitespace-nowrap px-2.5 py-1 rounded-md bg-slate-900 border border-emerald-500/30 hover:border-emerald-500 text-emerald-300 font-semibold text-[11px] transition-all flex items-center gap-1 cursor-pointer disabled:opacity-50"
            >
              <Code2 className="size-3 text-emerald-400" /> Review Approach
            </button>
            <button
              onClick={() => handleSendMessage('Why might my current code fail on edge cases?', 'hint')}
              disabled={loading}
              className="whitespace-nowrap px-2.5 py-1 rounded-md bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 font-semibold text-[11px] transition-all flex items-center gap-1 cursor-pointer disabled:opacity-50"
            >
              <HelpCircle className="size-3 text-slate-400" /> Edge Case Clue
            </button>
          </>
        ) : (
          <>
            <button
              onClick={() => handleSendMessage('Explain the bug in detail and why my code failed.', 'explanation')}
              disabled={loading}
              className="whitespace-nowrap px-2.5 py-1 rounded-md bg-slate-900 border border-amber-500/30 hover:border-amber-500 text-amber-300 font-semibold text-[11px] transition-all flex items-center gap-1 cursor-pointer disabled:opacity-50"
            >
              <AlertTriangle className="size-3 text-amber-400" /> Explain Bug
            </button>
            <button
              onClick={() => handleSendMessage('What is the correct optimal approach for this problem?', 'explanation')}
              disabled={loading}
              className="whitespace-nowrap px-2.5 py-1 rounded-md bg-slate-900 border border-emerald-500/30 hover:border-emerald-500 text-emerald-300 font-semibold text-[11px] transition-all flex items-center gap-1 cursor-pointer disabled:opacity-50"
            >
              <CheckCircle2 className="size-3 text-emerald-400" /> Correct Approach
            </button>
            <button
              onClick={() => handleSendMessage('What are the time and space complexity bounds?', 'explanation')}
              disabled={loading}
              className="whitespace-nowrap px-2.5 py-1 rounded-md bg-slate-900 border border-indigo-500/30 hover:border-indigo-500 text-indigo-300 font-semibold text-[11px] transition-all flex items-center gap-1 cursor-pointer disabled:opacity-50"
            >
              <Sparkles className="size-3 text-indigo-400" /> Complexity
            </button>
            <button
              onClick={() => handleSendMessage('Suggest a similar interview problem to practice next.', 'review')}
              disabled={loading}
              className="whitespace-nowrap px-2.5 py-1 rounded-md bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 font-semibold text-[11px] transition-all flex items-center gap-1 cursor-pointer disabled:opacity-50"
            >
              <ChevronRight className="size-3 text-slate-400" /> Similar Problem
            </button>
          </>
        )}
      </div>

      {/* Messages list */}
      <div className="flex-1 overflow-y-auto p-3.5 space-y-3.5">
        {messages.map((msg) => {
          const isUser = msg.role === 'user';
          return (
            <div
              key={msg.id}
              className={`flex flex-col ${isUser ? 'items-end' : 'items-start'}`}
            >
              <div
                className={`max-w-[90%] rounded-xl p-3 leading-relaxed ${
                  isUser
                    ? 'bg-indigo-600 text-white rounded-br-xs shadow-md'
                    : 'bg-[#111827] border border-slate-800 text-slate-200 rounded-bl-xs'
                }`}
              >
                {!isUser && msg.type && (
                  <div className="flex items-center gap-1.5 mb-1.5">
                    <span className={`text-[9px] font-bold uppercase tracking-wider px-1.5 py-0.5 rounded ${
                      msg.type === 'error-help' ? 'bg-rose-950/40 text-rose-300 border border-rose-900/30' :
                      msg.type === 'review' ? 'bg-emerald-950/40 text-emerald-300 border border-emerald-900/30' :
                      msg.type === 'explanation' ? 'bg-purple-950/40 text-purple-300 border border-purple-900/30' :
                      'bg-indigo-950/40 text-indigo-300 border border-indigo-900/30'
                    }`}>
                      {msg.type}
                    </span>
                  </div>
                )}
                <div className="whitespace-pre-wrap font-sans text-xs space-y-2">
                  {msg.content}
                </div>
              </div>
              <span className="text-[9px] text-slate-600 mt-1 px-1">{msg.timestamp}</span>
            </div>
          );
        })}

        {loading && (
          <div className="flex items-center gap-2 text-slate-400 p-2.5 bg-slate-900/40 border border-slate-800 rounded-xl w-fit">
            <span className="size-2 bg-indigo-500 rounded-full animate-ping"></span>
            <span className="text-[11px] font-medium text-slate-300">Analyzing your latest code...</span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Form */}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleSendMessage();
        }}
        className="p-2.5 bg-[#0e1626] border-t border-slate-800 flex items-center gap-2 shrink-0"
      >
        <input
          type="text"
          value={inputMessage}
          disabled={loading}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder={
            sessionMode === 'exam' && !isSubmitted
              ? "Ask about your latest code (conceptual guidance only)..."
              : "Ask about your latest code or test results..."
          }
          className="flex-1 bg-[#070b13] border border-slate-800 rounded-lg px-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
        />
        <button
          type="submit"
          disabled={loading || !inputMessage.trim()}
          className="p-2 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white rounded-lg transition-all cursor-pointer shadow-[0_0_10px_rgba(99,102,241,0.2)]"
        >
          <Send className="size-3.5" />
        </button>
      </form>
    </div>
  );
}
