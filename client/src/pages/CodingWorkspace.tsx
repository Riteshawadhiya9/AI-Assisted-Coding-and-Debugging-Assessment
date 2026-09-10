import { useState, useEffect } from 'react';
import { useSearchParams, useNavigate, Link } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import {
  Play, RotateCcw, Sparkles, BookOpen, CheckCircle2,
  XCircle, Clock, AlertCircle, Terminal, ChevronUp, ChevronDown,
  ArrowLeft, Check, Code2
} from 'lucide-react';
import type { CodingQuestion, CodingLanguage, CodingExecutionResult, CodingTestCase } from '../types';
import CodingAIPanel from '../components/CodingAIPanel';

export default function CodingWorkspace() {
  const [searchParams, setSearchParams] = useSearchParams();
  const navigate = useNavigate();

  const questionId = searchParams.get('id') || 'cq-1';
  const urlLang = (searchParams.get('lang') as CodingLanguage) || 'python';
  const mode = (searchParams.get('mode') as 'practice' | 'assessment') || 'practice';

  const [question, setQuestion] = useState<CodingQuestion | null>(null);
  const [language, setLanguage] = useState<CodingLanguage>(urlLang);
  const [code, setCode] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Right Side Tabs: 'problem' | 'ai'
  const [rightTab, setRightTab] = useState<'problem' | 'ai'>('problem');

  // Execution & Bottom Panel State
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [executionResult, setExecutionResult] = useState<CodingExecutionResult | null>(null);
  const [selectedTestCaseIndex, setSelectedTestCaseIndex] = useState<number>(0);
  const [showConsole, setShowConsole] = useState<boolean>(true);

  // Timer
  const [elapsedSeconds, setElapsedSeconds] = useState<number>(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setElapsedSeconds(prev => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const formatTime = (secs: number) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // Fetch Question
  useEffect(() => {
    async function loadQuestion() {
      setLoading(true);
      setError(null);
      try {
        let targetId = questionId;
        if (!targetId || targetId === 'cq-1') {
          const listRes = await fetch('/api/coding/questions');
          if (listRes.ok) {
            const list = await listRes.json();
            if (list && list.length > 0) {
              targetId = list[0].id;
            }
          }
        }
        const res = await fetch(`/api/coding/questions/${targetId}`);
        if (!res.ok) {
          throw new Error(`Failed to load coding question #${targetId}`);
        }
        const data: CodingQuestion = await res.json();
        setQuestion(data);
        const initialCode = data.starterCode?.[language] || data.starterCode?.['python'] || '# Write your solution here';
        setCode(initialCode);
      } catch (err: any) {
        setError(err.message || 'Error loading question');
      } finally {
        setLoading(false);
      }
    }
    loadQuestion();
  }, [questionId]);

  // Handle Language Switching
  const handleLanguageChange = (newLang: CodingLanguage) => {
    setLanguage(newLang);
    if (question && question.starterCode?.[newLang]) {
      setCode(question.starterCode[newLang]);
    }
    const params = new URLSearchParams(searchParams);
    params.set('lang', newLang);
    setSearchParams(params, { replace: true });
  };

  // Reset Code
  const handleReset = () => {
    if (!question) return;
    if (window.confirm('Reset code to default starter template? Current changes will be discarded.')) {
      const resetCode = question.starterCode?.[language] || '';
      setCode(resetCode);
      setExecutionResult(null);
    }
  };

  // Run Code
  const handleRunCode = async () => {
    if (!question || isRunning) return;
    setIsRunning(true);
    setShowConsole(true);
    try {
      const res = await fetch('/api/coding/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          questionId: question.id,
          code,
          language
        })
      });
      if (!res.ok) throw new Error('Execution request failed');
      const data: CodingExecutionResult = await res.json();
      setExecutionResult(data);
      setSelectedTestCaseIndex(0);
    } catch (err: any) {
      const fallbackTests = question.testCases || question.visibleTestCases || [];
      setExecutionResult({
        passed: false,
        passedCount: 0,
        totalCount: fallbackTests.length,
        testCases: fallbackTests.map(tc => ({
          ...tc,
          passed: false,
          actualOutput: `Error: ${err.message || 'Execution failed'}`
        })),
        executionTimeMs: 0,
        runtimeOutput: err.message
      });
    } finally {
      setIsRunning(false);
    }
  };

  // Submit Code
  const handleSubmitCode = async () => {
    if (!question || isSubmitting) return;
    setIsSubmitting(true);
    try {
      const res = await fetch('/api/coding/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          questionId: question.id,
          code,
          language,
          mode,
          timeSpentSeconds: elapsedSeconds
        })
      });
      if (!res.ok) throw new Error('Submission failed');
      const result = await res.json();
      
      // Store in localStorage for Results page
      sessionStorage.setItem('last_coding_result', JSON.stringify(result));
      navigate(`/coding/results?id=${question.id}`);
    } catch (err: any) {
      alert(`Submission error: ${err.message || 'Failed to submit'}`);
      setIsSubmitting(false);
    }
  };

  // Monaco Editor Language mapping
  const getMonacoLang = (lang: CodingLanguage): string => {
    switch (lang) {
      case 'python': return 'python';
      case 'javascript': return 'javascript';
      case 'typescript': return 'typescript';
      case 'java': return 'java';
      case 'cpp': return 'cpp';
      default: return 'python';
    }
  };

  if (loading) {
    return (
      <div className="flex-1 grid place-items-center bg-[#0b0f19] text-slate-300">
        <div className="flex flex-col items-center gap-3">
          <div className="size-10 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin" />
          <p className="text-sm font-medium text-slate-400">Loading AI-Assisted Coding Workspace...</p>
        </div>
      </div>
    );
  }

  if (error || !question) {
    return (
      <div className="flex-1 grid place-items-center bg-[#0b0f19] p-6">
        <div className="max-w-md w-full bg-slate-900 border border-slate-800 rounded-xl p-6 text-center">
          <AlertCircle className="size-10 text-rose-500 mx-auto mb-3" />
          <h2 className="text-lg font-bold text-white mb-2">Question Not Found</h2>
          <p className="text-xs text-slate-400 mb-6">{error || 'Could not load problem data.'}</p>
          <Link
            to="/coding/setup"
            className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-semibold"
          >
            <ArrowLeft className="size-4" />
            Back to Coding Setup
          </Link>
        </div>
      </div>
    );
  }

  const activeTestCases: CodingTestCase[] = executionResult?.testCases || question.testCases || question.visibleTestCases || [];
  const currentSelectedTest = activeTestCases[selectedTestCaseIndex] || activeTestCases[0];

  return (
    <div className="flex-1 flex flex-col h-[calc(100vh-61px)] bg-[#0b0f19] overflow-hidden">
      {/* Top Action Bar */}
      <div className="h-12 border-b border-slate-800 bg-[#0d1322] px-4 flex items-center justify-between shrink-0">
        <div className="flex items-center gap-3">
          <Link
            to="/coding/setup"
            className="flex items-center gap-1.5 text-xs text-slate-400 hover:text-white bg-slate-800/60 hover:bg-slate-800 px-2.5 py-1.5 rounded-md border border-slate-700/50 transition-colors"
          >
            <ArrowLeft className="size-3.5" />
            <span>Setup</span>
          </Link>
          <div className="h-4 w-px bg-slate-800" />
          <div className="flex items-center gap-2">
            <span className="text-sm font-bold text-white">
              {question.number ? `${question.number}. ` : ''}{question.title}
            </span>
            <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${
              (question.difficulty || '').toLowerCase() === 'easy' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' :
              (question.difficulty || '').toLowerCase() === 'medium' ? 'bg-amber-500/10 text-amber-400 border-amber-500/20' :
              'bg-rose-500/10 text-rose-400 border-rose-500/20'
            }`}>
              {(question.difficulty || 'Medium').charAt(0).toUpperCase() + (question.difficulty || 'Medium').slice(1)}
            </span>
            <span className="text-[10px] text-slate-400 bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700/40">
              {question.topic}
            </span>
          </div>
        </div>

        {/* Center & Right Controls */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1.5 text-xs text-slate-400 bg-slate-900/80 border border-slate-800 px-3 py-1 rounded-md">
            <Clock className="size-3.5 text-indigo-400" />
            <span className="font-mono">{formatTime(elapsedSeconds)}</span>
          </div>

          <button
            onClick={handleReset}
            className="flex items-center gap-1.5 text-xs text-slate-400 hover:text-white bg-slate-800/50 hover:bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-700/50 transition-colors"
            title="Reset code to original starter code"
          >
            <RotateCcw className="size-3.5" />
            <span>Reset</span>
          </button>

          <button
            onClick={handleRunCode}
            disabled={isRunning}
            className="flex items-center gap-1.5 text-xs font-semibold text-slate-200 hover:text-white bg-slate-800 hover:bg-slate-700 px-3.5 py-1.5 rounded-lg border border-slate-600/60 transition-colors disabled:opacity-50"
          >
            <Play className={`size-3.5 text-emerald-400 ${isRunning ? 'animate-spin' : ''}`} />
            <span>{isRunning ? 'Running...' : 'Run Code'}</span>
          </button>

          <button
            onClick={handleSubmitCode}
            disabled={isSubmitting}
            className="flex items-center gap-1.5 text-xs font-bold text-white bg-emerald-600 hover:bg-emerald-500 px-4 py-1.5 rounded-lg shadow-sm transition-colors disabled:opacity-50"
          >
            <Check className="size-3.5" />
            <span>{isSubmitting ? 'Submitting...' : 'Submit'}</span>
          </button>
        </div>
      </div>

      {/* Main Two-Column Workspace (Full Available Screen) */}
      <div className="flex-1 flex overflow-hidden">
        {/* ========================================================= */}
        {/* LEFT COLUMN: Coding IDE (Monaco Editor & Bottom Test Results) */}
        {/* ========================================================= */}
        <div className="flex-1 flex flex-col min-w-0 border-r border-slate-800 bg-[#0d1322] h-full overflow-hidden">
          {/* Editor Header: Language selector */}
          <div className="h-9 px-3 border-b border-slate-800/80 bg-[#0f172a] flex items-center justify-between shrink-0">
            <div className="flex items-center gap-2">
              <Code2 className="size-4 text-indigo-400" />
              <span className="text-xs font-semibold text-slate-300">Code Editor</span>
            </div>

            <div className="flex items-center gap-2">
              <span className="text-[11px] text-slate-400">Language:</span>
              <select
                value={language}
                onChange={(e) => handleLanguageChange(e.target.value as CodingLanguage)}
                className="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded px-2 py-0.5 focus:outline-none focus:border-indigo-500"
              >
                <option value="python">Python 3</option>
                <option value="javascript">JavaScript (Node.js)</option>
                <option value="typescript">TypeScript</option>
                <option value="java">Java</option>
                <option value="cpp">C++</option>
              </select>
            </div>
          </div>

          {/* Monaco Editor Container */}
          <div className="flex-1 min-h-0 relative">
            <Editor
              height="100%"
              language={getMonacoLang(language)}
              value={code}
              theme="vs-dark"
              onChange={(newVal) => setCode(newVal || '')}
              options={{
                fontSize: 13,
                minimap: { enabled: false },
                scrollBeyondLastLine: false,
                tabSize: 4,
                automaticLayout: true,
                padding: { top: 12, bottom: 12 },
                lineNumbers: 'on',
                fontFamily: `'Fira Code', 'Consolas', monospace`
              }}
            />
          </div>

          {/* Collapsible Test Case & Results Panel */}
          <div className={`border-t border-slate-800 bg-[#0a0f1d] flex flex-col transition-all duration-200 ${
            showConsole ? 'h-64' : 'h-8'
          }`}>
            {/* Panel Header Bar */}
            <div
              onClick={() => setShowConsole(!showConsole)}
              className="h-8 px-3 bg-[#0f172a]/90 border-b border-slate-800/60 flex items-center justify-between cursor-pointer select-none"
            >
              <div className="flex items-center gap-2">
                <Terminal className="size-3.5 text-indigo-400" />
                <span className="text-xs font-semibold text-slate-300">
                  Test Cases & Execution Results
                </span>
                {executionResult && (
                  <span className={`text-[10px] px-2 py-0.2 rounded-full font-bold ml-2 ${
                    executionResult.passed
                      ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                      : 'bg-rose-500/20 text-rose-400 border border-rose-500/30'
                  }`}>
                    {executionResult.passedCount} / {executionResult.totalCount} Passed
                  </span>
                )}
              </div>

              <div className="flex items-center gap-1 text-slate-400 hover:text-white">
                {showConsole ? <ChevronDown className="size-4" /> : <ChevronUp className="size-4" />}
              </div>
            </div>

            {/* Panel Body */}
            {showConsole && (
              <div className="flex-1 flex min-h-0">
                {/* Test case tabs */}
                <div className="w-40 border-r border-slate-800/80 p-2 flex flex-col gap-1 overflow-y-auto bg-slate-950/40">
                  {activeTestCases.map((tc, idx) => (
                    <button
                      key={tc.id || idx}
                      onClick={() => setSelectedTestCaseIndex(idx)}
                      className={`flex items-center justify-between px-2.5 py-1.5 rounded text-xs transition-colors text-left ${
                        selectedTestCaseIndex === idx
                          ? 'bg-indigo-600/30 text-indigo-200 border border-indigo-500/40 font-semibold'
                          : 'text-slate-400 hover:bg-slate-800/50 hover:text-slate-200'
                      }`}
                    >
                      <span>Case {idx + 1}</span>
                      {tc.passed !== undefined && (
                        tc.passed ? (
                          <CheckCircle2 className="size-3 text-emerald-400" />
                        ) : (
                          <XCircle className="size-3 text-rose-400" />
                        )
                      )}
                    </button>
                  ))}
                </div>

                {/* Test Case Details */}
                <div className="flex-1 p-3 overflow-y-auto space-y-3 font-mono text-xs">
                  {currentSelectedTest ? (
                    <>
                      <div>
                        <div className="text-[10px] font-sans uppercase font-bold text-slate-400 tracking-wider mb-1">
                          Input:
                        </div>
                        <div className="bg-slate-900 border border-slate-800 rounded p-2 text-slate-200">
                          {currentSelectedTest.input}
                        </div>
                      </div>

                      <div className="grid grid-cols-2 gap-3">
                        <div>
                          <div className="text-[10px] font-sans uppercase font-bold text-slate-400 tracking-wider mb-1">
                            Expected Output:
                          </div>
                          <div className="bg-slate-900 border border-slate-800 rounded p-2 text-emerald-300">
                            {currentSelectedTest.expectedOutput}
                          </div>
                        </div>

                        <div>
                          <div className="text-[10px] font-sans uppercase font-bold text-slate-400 tracking-wider mb-1">
                            Actual Output:
                          </div>
                          <div className={`bg-slate-900 border rounded p-2 ${
                            currentSelectedTest.passed === undefined
                              ? 'border-slate-800 text-slate-500'
                              : currentSelectedTest.passed
                              ? 'border-emerald-500/40 text-emerald-300'
                              : 'border-rose-500/40 text-rose-300'
                          }`}>
                            {currentSelectedTest.actualOutput !== undefined
                              ? currentSelectedTest.actualOutput
                              : 'Click "Run Code" to view output'}
                          </div>
                        </div>
                      </div>

                      {currentSelectedTest.explanation && (
                        <div>
                          <div className="text-[10px] font-sans uppercase font-bold text-slate-400 tracking-wider mb-1">
                            Explanation:
                          </div>
                          <div className="text-slate-300 font-sans text-xs bg-slate-900/50 p-2 rounded border border-slate-800">
                            {currentSelectedTest.explanation}
                          </div>
                        </div>
                      )}
                    </>
                  ) : (
                    <div className="text-slate-500 text-xs">Select a test case to inspect details.</div>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* ========================================================= */}
        {/* RIGHT COLUMN: Tabbed Problem & AI Assistant */}
        {/* ========================================================= */}
        <div className="w-[45%] flex flex-col min-w-[360px] max-w-[650px] bg-[#0c1220] h-full overflow-hidden">
          {/* Tab Selection Bar: [Problem] [AI Assistant] */}
          <div className="h-10 border-b border-slate-800 bg-[#0f172a] px-3 flex items-center justify-between shrink-0">
            <div className="flex items-center gap-1">
              <button
                onClick={() => setRightTab('problem')}
                className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-md transition-colors ${
                  rightTab === 'problem'
                    ? 'bg-indigo-600 text-white shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
                }`}
              >
                <BookOpen className="size-3.5" />
                <span>Problem</span>
              </button>

              <button
                onClick={() => setRightTab('ai')}
                className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-md transition-colors ${
                  rightTab === 'ai'
                    ? 'bg-indigo-600 text-white shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
                }`}
              >
                <Sparkles className="size-3.5 text-amber-400" />
                <span>AI Assistant</span>
              </button>
            </div>

            <div className="text-[11px] text-slate-400">
              {rightTab === 'problem' ? 'LeetCode Standard' : 'Real-time Mentor'}
            </div>
          </div>

          {/* Right Tab Content */}
          <div className="flex-1 min-h-0 overflow-hidden">
            {rightTab === 'problem' ? (
              <div className="h-full overflow-y-auto p-5 space-y-6 text-slate-200">
                {/* Header info */}
                <div>
                  <h1 className="text-lg font-bold text-white mb-2">
                    {question.number ? `${question.number}. ` : ''}{question.title}
                  </h1>
                  <div className="flex items-center gap-2">
                    <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full border ${
                      (question.difficulty || '').toLowerCase() === 'easy' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' :
                      (question.difficulty || '').toLowerCase() === 'medium' ? 'bg-amber-500/10 text-amber-400 border-amber-500/20' :
                      'bg-rose-500/10 text-rose-400 border-rose-500/20'
                    }`}>
                      {(question.difficulty || 'Medium').charAt(0).toUpperCase() + (question.difficulty || 'Medium').slice(1)}
                    </span>
                    <span className="text-[11px] text-slate-400 bg-slate-800 px-2 py-0.5 rounded">
                      {question.topic}
                    </span>
                  </div>
                </div>

                {/* Problem Description */}
                <div>
                  <h2 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">
                    Problem Description
                  </h2>
                  <div className="text-xs leading-relaxed text-slate-300 space-y-3 whitespace-pre-wrap">
                    {question.problemStatement || question.description}
                  </div>
                </div>

                {/* Examples */}
                {question.examples && question.examples.length > 0 && (
                  <div className="space-y-4">
                    <h2 className="text-xs font-bold uppercase tracking-wider text-slate-400">
                      Examples
                    </h2>
                    {question.examples.map((ex, idx) => (
                      <div key={idx} className="bg-slate-900/90 border border-slate-800 rounded-lg p-3.5 space-y-2">
                        <div className="text-xs font-bold text-indigo-300">
                          Example {idx + 1}
                        </div>
                        <div className="font-mono text-xs text-slate-200">
                          <span className="font-sans font-bold text-slate-400 mr-2">Input:</span>
                          <span className="bg-slate-950 px-2 py-0.5 rounded border border-slate-800">{ex.input}</span>
                        </div>
                        <div className="font-mono text-xs text-slate-200">
                          <span className="font-sans font-bold text-slate-400 mr-2">Output:</span>
                          <span className="bg-slate-950 px-2 py-0.5 rounded border border-slate-800 text-emerald-300">{ex.output}</span>
                        </div>
                        {ex.explanation && (
                          <div className="text-xs text-slate-400 font-sans mt-1">
                            <span className="font-bold text-slate-300 mr-1">Explanation:</span>
                            {ex.explanation}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                )}

                {/* Constraints */}
                {question.constraints && question.constraints.length > 0 && (
                  <div>
                    <h2 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">
                      Constraints
                    </h2>
                    <ul className="list-disc list-inside space-y-1 text-xs text-slate-300 font-mono">
                      {question.constraints.map((c, idx) => (
                        <li key={idx} className="leading-relaxed">
                          <span className="font-mono">{c}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ) : (
              <CodingAIPanel
                question={question}
                language={language}
                currentCode={code}
                mode={mode}
              />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
