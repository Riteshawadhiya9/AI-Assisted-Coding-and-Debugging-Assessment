import { useState, useEffect, useRef, Fragment } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import { 
  Play, Send, RotateCcw, AlertTriangle, 
  Clock, X, CheckCircle2, XCircle, Search, Bug as BugIcon, 
  History, HelpCircle, ArrowRight, Sparkles, ListFilter, Bot
} from 'lucide-react';
import type { 
  Question, TestCase, Attempt, BugType, 
  UserDiagnosis, RunHistoryItem, ScoreBreakdown, Language 
} from '../types';
import VisualDiagram from '../components/VisualDiagram';
import AIAssistantPanel, { type ChatMessage } from '../components/AIAssistantPanel';

const BUG_TYPES: BugType[] = [
  'boundary',
  'off-by-one',
  'incorrect condition',
  'incorrect initialization',
  'incorrect recursion',
  'incorrect traversal',
  'incorrect state transition',
  'incorrect data structure usage',
  'logical',
  'edge case',
  'integer overflow',
  'time complexity',
  'runtime',
  'compilation',
  'syntax'
];

export default function Workspace() {
  const [searchParams, setSearchParams] = useSearchParams();
  const navigate = useNavigate();

  // Query parameters
  const questionId = searchParams.get('id') || 'q_tree_max_depth';
  const sessionMode = (searchParams.get('mode') as 'practice' | 'exam') || 'practice';
  const urlLang = (searchParams.get('lang') as Language) || 'cpp';

  // State variables
  const [question, setQuestion] = useState<Question | null>(null);
  const [selectedLanguage, setSelectedLanguage] = useState<Language>(urlLang);
  const [code, setCode] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Workflow steps: Review -> Identify -> Fix -> Validate
  const [activeStep, setActiveStep] = useState<'review' | 'identify' | 'fix' | 'validate'>('review');

  // Diagnosis State (Step 2)
  const [userDiagnosis, setUserDiagnosis] = useState<UserDiagnosis>({
    bugType: '',
    notes: '',
    isLocked: false
  });

  // Run History & Execution State
  const [runHistory, setRunHistory] = useState<RunHistoryItem[]>([]);
  const [activePanel, setActivePanel] = useState<'tests' | 'identify' | 'ai' | 'history' | 'hints'>('tests');
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [isFetchingNext, setIsFetchingNext] = useState<boolean>(false);
  const [consoleLogs, setConsoleLogs] = useState<string>('[Local Mock Sandbox] Ready. Click "Run Code" to execute test cases.');
  const [testCases, setTestCases] = useState<TestCase[]>([]);
  const [selectedTestId, setSelectedTestId] = useState<number>(1);
  const [hintsUsed, setHintsUsed] = useState<number>(0);
  const [showConfirmSubmit, setShowConfirmSubmit] = useState<boolean>(false);
  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);

  // Real-time Code Tracking & Multi-turn Conversation Context for AI
  const [originalBuggyCode, setOriginalBuggyCode] = useState<string>('');
  const [lastRunCode, setLastRunCode] = useState<string>('');
  const [lastSubmittedCode, setLastSubmittedCode] = useState<string>('');
  const [latestExecutionResult, setLatestExecutionResult] = useState<any>(null);
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([]);

  // Timing
  const [elapsedSeconds, setElapsedSeconds] = useState<number>(0);
  const [timeLeft, setTimeLeft] = useState<number>(1200); // 20 minutes in seconds for Exam mode
  const [timerWarning, setTimerWarning] = useState<string | null>(null);
  const startTimeRef = useRef<number>(0);
  const deadlineRef = useRef<number | null>(null);
  const timerIntervalRef = useRef<any>(null);

  // Helper to compute human-readable line diff between original and current code
  const computeCodeDiff = (original: string, current: string): string => {
    if (!original || !current || original === current) {
      return 'No modifications made yet. Editor code matches initial buggy code.';
    }
    const origLines = original.split('\n');
    const currLines = current.split('\n');
    const diffs: string[] = [];
    const maxL = Math.max(origLines.length, currLines.length);
    for (let i = 0; i < maxL; i++) {
      const o = origLines[i];
      const c = currLines[i];
      if (o !== c) {
        if (o !== undefined && c !== undefined) {
          diffs.push(`Line ${i + 1}:\n- ${o}\n+ ${c}`);
        } else if (o === undefined) {
          diffs.push(`Line ${i + 1} (added):\n+ ${c}`);
        } else {
          diffs.push(`Line ${i + 1} (removed):\n- ${o}`);
        }
      }
      if (diffs.length >= 8) {
        diffs.push('... (additional changes truncated)');
        break;
      }
    }
    return diffs.join('\n\n');
  };

  // Submit attempt
  const submitCode = async (_isAuto = false) => {
    if (!question || isSubmitting) return;
    setIsSubmitting(true);
    setIsSubmitted(true);
    setShowConfirmSubmit(false);
    setLastSubmittedCode(code);

    try {
      const res = await fetch(`/api/questions/${question.id}/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          code, 
          language: selectedLanguage,
          isSubmission: true,
          userDiagnosis: {
            bugType: userDiagnosis.bugType,
            notes: userDiagnosis.notes
          }
        })
      });

      if (!res.ok) throw new Error('Submission execution failed');
      const runResult = await res.json();

      const totalTests = runResult.testResults.length;
      const passedTests = runResult.testResults.filter((r: any) => r.passed).length;
      const isFixed = runResult.passed;

      const timeSpent = sessionMode === 'exam'
        ? 1200 - timeLeft
        : Math.floor((Date.now() - (startTimeRef.current || Date.now())) / 1000);

      // Scoring Breakdown Calculation
      const correctnessScore = isFixed ? 50 : 0;
      const testScore = Math.round((passedTests / Math.max(1, totalTests)) * 20);
      const diagnosisScore = runResult.diagnosisCorrect 
        ? 20 
        : (userDiagnosis.notes.trim().length >= 10 ? 10 : 0);
      const estimatedSecs = (question.estimatedTime || 20) * 60;
      const timeBonus = (timeSpent <= estimatedSecs) ? 10 : (timeSpent <= estimatedSecs * 1.5 ? 5 : 0);
      const hintsPenalty = sessionMode === 'practice' ? Math.min(10, hintsUsed * 5) : 0;

      const calculatedFinal = Math.max(0, Math.min(100, 
        correctnessScore + testScore + diagnosisScore + timeBonus - hintsPenalty
      ));

      const breakdown: ScoreBreakdown = {
        correctness: correctnessScore,
        tests: testScore,
        diagnosis: diagnosisScore,
        timeBonus,
        hintsPenalty,
        finalScore: calculatedFinal
      };

      const attempt: Attempt = {
        id: 'att_' + Date.now(),
        questionId: question.id,
        questionTitle: question.title,
        language: selectedLanguage,
        difficulty: question.difficulty,
        topic: question.topic,
        mode: sessionMode,
        score: calculatedFinal,
        timeSpentSeconds: timeSpent,
        status: isFixed ? 'passed' : 'failed',
        date: new Date().toLocaleDateString(),
        codeSubmitted: code,
        bugsDiagnosed: userDiagnosis.bugType ? [userDiagnosis.bugType] : [],
        diagnosedBugType: userDiagnosis.bugType,
        diagnosisNotes: userDiagnosis.notes,
        diagnosisCorrect: runResult.diagnosisCorrect,
        scoreBreakdown: breakdown,
        testsPassed: passedTests,
        totalTests: totalTests
      };

      // Save attempt in localStorage
      const existingStr = localStorage.getItem('debuglab_attempts');
      const existing: Attempt[] = existingStr ? JSON.parse(existingStr) : [];
      existing.unshift(attempt);
      localStorage.setItem('debuglab_attempts', JSON.stringify(existing));

      setTimeout(() => {
        setIsSubmitting(false);
        navigate(`/results?attemptId=${attempt.id}`);
      }, 700);
    } catch (err: any) {
      alert(`Submission failed: ${err.message || err}`);
      setIsSubmitting(false);
    }
  };


  const handleAutoSubmit = () => {
    setTimerWarning('Time is up! Auto-submitting your code...');
    setTimeout(() => {
      submitCode(true);
    }, 1500);
  };

  // Handle Language Switching
  const handleLanguageChange = (lang: Language) => {
    if (lang === selectedLanguage) return;
    setSelectedLanguage(lang);
    if (question) {
      const newCode = question.implementations?.[lang]?.buggyCode || question.buggyCode || '';
      setCode(newCode);
      setOriginalBuggyCode(newCode);
      setLastRunCode('');
      setLatestExecutionResult(null);
      // Reset tests for new language
      setTestCases(question.visibleTestCases.map(tc => ({ ...tc, passed: undefined, actualOutput: undefined })));
      setConsoleLogs(`[Local Mock Sandbox] Switched language mode to ${lang.toUpperCase()}.\nReady. Click "Run Code" to execute test cases.`);
      setChatMessages([
        {
          id: `welcome-${lang}-${Date.now()}`,
          role: 'assistant',
          content: sessionMode === 'exam'
            ? `🛡️ **Exam Mode AI Proctor Ready.**\n\nSwitched to **${lang.toUpperCase()}**. Analyzing your current code for **${question.title}**. Under assessment policy, I cannot reveal direct bug locations, fixes, or solutions until you submit.`
            : `👋 **AI Debugging Mentor Active.**\n\nSwitched to **${lang.toUpperCase()}**. Analyzing your current Monaco editor code for **${question.title}**. Ask for hints, request an error breakdown, or have me review your approach.`,
          type: 'hint',
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }
      ]);
    }
    const newParams = new URLSearchParams(searchParams);
    newParams.set('lang', lang);
    setSearchParams(newParams, { replace: true });
  };

  // Fetch question details
  useEffect(() => {
    async function fetchQuestion() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`/api/questions/${questionId}`);
        if (!res.ok) {
          throw new Error(`Question '${questionId}' was not found in the question bank.`);
        }
        const data: Question = await res.json();
        setQuestion(data);
        const initialCode = data.implementations?.[selectedLanguage]?.buggyCode || data.buggyCode || '';
        setCode(initialCode);
        setOriginalBuggyCode(initialCode);
        setLastRunCode('');
        setLatestExecutionResult(null);
        setTestCases(data.visibleTestCases.map(tc => ({ ...tc, passed: undefined, actualOutput: undefined })));
        setSelectedTestId(data.visibleTestCases[0]?.id || 1);
        startTimeRef.current = Date.now();
        setElapsedSeconds(0);
        setRunHistory([]);
        setUserDiagnosis({ bugType: '', notes: '', isLocked: false });
        setActiveStep('review');
        setActivePanel('tests');
        setChatMessages([
          {
            id: `welcome-${Date.now()}`,
            role: 'assistant',
            content: sessionMode === 'exam'
              ? `🛡️ **Exam Mode AI Proctor Ready.**\n\nI can clarify runtime/compiler logs and offer conceptual hints for **${data.title}** in **${selectedLanguage.toUpperCase()}**. Under assessment policy, I cannot reveal direct bug locations, fixes, or solutions until you submit.`
              : `👋 **AI Debugging Mentor Active.**\n\nI'm here to help you debug **${data.title}** in **${selectedLanguage.toUpperCase()}**. Your current Monaco editor code is my source of truth. As you modify the code, I will analyze your changes in real time.`,
            type: 'hint',
            timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
          }
        ]);
      } catch (err: any) {
        setError(err.message || 'Failed to load question details.');
      } finally {
        setLoading(false);
      }
    }
    fetchQuestion();
  }, [questionId]);

  // Practice & Exam Timer
  useEffect(() => {
    if (loading || !question) return;

    if (sessionMode === 'exam') {
      const durationMs = 20 * 60 * 1000;
      const deadline = Date.now() + durationMs;
      deadlineRef.current = deadline;

      const updateExamTimer = () => {
        const remainingMs = deadline - Date.now();
        if (remainingMs <= 0) {
          setTimeLeft(0);
          if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
          handleAutoSubmit();
        } else {
          const remainingSecs = Math.round(remainingMs / 1000);
          setTimeLeft(remainingSecs);

          if (remainingSecs === 600) setTimerWarning('10:00 remaining in exam!');
          else if (remainingSecs === 300) setTimerWarning('5:00 remaining! Wrap up your fix.');
          else if (remainingSecs === 60) setTimerWarning('1:00 remaining! Finalizing checks.');
        }
      };

      updateExamTimer();
      timerIntervalRef.current = setInterval(updateExamTimer, 1000);
    } else {
      // Practice mode upward counter
      timerIntervalRef.current = setInterval(() => {
        if (startTimeRef.current) {
          setElapsedSeconds(Math.floor((Date.now() - startTimeRef.current) / 1000));
        }
      }, 1000);
    }

    return () => {
      if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    };
  }, [sessionMode, loading, question]);

  // Run Code against execution provider
  const handleRun = async () => {
    if (!question || isRunning || isSubmitting) return;
    setIsRunning(true);
    setActivePanel('tests');
    setLastRunCode(code);
    setConsoleLogs(prev => prev + `\n\n> [${new Date().toLocaleTimeString()}] Executing test runner for ${selectedLanguage.toUpperCase()}...\n`);

    try {
      const res = await fetch(`/api/questions/${question.id}/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          code, 
          language: selectedLanguage,
          isSubmission: false,
          userDiagnosis: userDiagnosis.isLocked ? {
            bugType: userDiagnosis.bugType,
            notes: userDiagnosis.notes
          } : undefined
        })
      });

      if (!res.ok) throw new Error('Execution endpoint returned failure status');
      const runResult = await res.json();

      setTimeout(() => {
        const updatedTestCases = testCases.map(tc => {
          const matchingResult = runResult.testResults.find((r: any) => r.testCaseId === tc.id);
          return {
            ...tc,
            passed: matchingResult ? matchingResult.passed : false,
            actualOutput: matchingResult ? matchingResult.actualOutput : 'Execution missing'
          };
        });

        const passedCount = updatedTestCases.filter(t => t.passed).length;
        const totalCount = updatedTestCases.length;

        // Record execution outcome for AI context
        const executionOutcome = {
          status: runResult.passed ? 'passed' : 'failed',
          passedCount,
          totalCount,
          compileOutput: runResult.compileOutput || 'Compiled cleanly',
          runtimeOutput: runResult.runtimeOutput || `Ran ${totalCount} visible tests`,
          errorDetails: runResult.passed ? undefined : (runResult.compileOutput || 'Test assertion mismatch'),
          testResultsSummary: `${passedCount}/${totalCount} visible test cases passed.`
        };
        setLatestExecutionResult(executionOutcome);

        // Add to Run History
        const newHistoryItem: RunHistoryItem = {
          id: Date.now(),
          timestamp: new Date().toLocaleTimeString(),
          passed: runResult.passed,
          passedCount,
          totalCount,
          compileOutput: runResult.compileOutput || 'Compiled cleanly',
          runtimeOutput: runResult.runtimeOutput || `Ran ${totalCount} visible tests`,
          executionTimeMs: runResult.executionTimeMs || 15
        };

        setRunHistory(prev => [newHistoryItem, ...prev]);
        setTestCases(updatedTestCases);
        setIsRunning(false);
        setActivePanel('tests');

        setConsoleLogs(prev => 
          prev + `${runResult.compileOutput}\n${runResult.runtimeOutput}\nFinished in ${runResult.executionTimeMs}ms.\n`
        );

        if (activeStep === 'review' || activeStep === 'identify' || activeStep === 'fix') {
          setActiveStep('validate');
        }
      }, 350);
    } catch (err: any) {
      setConsoleLogs(prev => prev + `\n[ERROR] Execution error: ${err.message || err}\n`);
      setIsRunning(false);
    }
  };

  const handleResetCode = () => {
    if (!question) return;
    const initialBuggy = question.implementations?.[selectedLanguage]?.buggyCode || question.buggyCode || '';
    if (window.confirm(`Reset code to initial buggy implementation for ${selectedLanguage.toUpperCase()}? All edits will be lost.`)) {
      setCode(initialBuggy);
      setOriginalBuggyCode(initialBuggy);
      setLastRunCode('');
      setLatestExecutionResult(null);
      setActiveStep('identify');
    }
  };

  const handleNextQuestion = async () => {
    if (isFetchingNext || !question) return;
    setIsFetchingNext(true);
    try {
      const res = await fetch(`/api/questions/random?topic=${question.topic}&language=${selectedLanguage}`);
      if (res.ok) {
        const nextQ = await res.json();
        navigate(`/workspace?id=${nextQ.id}&mode=${sessionMode}&lang=${selectedLanguage}`);
      } else {
        const anyRes = await fetch('/api/questions/random');
        if (anyRes.ok) {
          const nextAny = await anyRes.json();
          navigate(`/workspace?id=${nextAny.id}&mode=${sessionMode}&lang=${selectedLanguage}`);
        }
      }
    } catch (err) {
      console.error(err);
    } finally {
      setIsFetchingNext(false);
    }
  };

  if (loading) {
    return (
      <div className="flex h-[80vh] items-center justify-center text-slate-400">
        <div className="text-center space-y-4">
          <span className="relative flex h-8 w-8 mx-auto">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-8 w-8 bg-indigo-500"></span>
          </span>
          <p className="text-sm font-semibold">Loading Problem Workspace...</p>
        </div>
      </div>
    );
  }

  if (error || !question) {
    return (
      <div className="flex h-[80vh] items-center justify-center text-rose-400 p-6">
        <div className="text-center space-y-4 max-w-md">
          <AlertTriangle className="size-12 mx-auto text-rose-500" />
          <h2 className="text-lg font-bold text-white">Problem Unavailable</h2>
          <p className="text-sm text-slate-400">{error || 'Unable to load workspace. Return to problems list.'}</p>
          <div className="flex gap-3 justify-center">
            <button 
              onClick={() => navigate('/problems')}
              className="px-4 py-2 bg-indigo-600 rounded-lg text-white font-semibold text-xs hover:bg-indigo-500 cursor-pointer"
            >
              Browse Problems
            </button>
            <button 
              onClick={() => navigate('/')}
              className="px-4 py-2 bg-slate-800 rounded-lg text-slate-300 font-semibold text-xs hover:bg-slate-700 cursor-pointer"
            >
              Dashboard
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full flex flex-col h-[calc(100vh-61px)] select-none bg-[#070b13]">
      {/* 1. Header Bar: Meta Info, Workflow Stepper, Controls */}
      <div className="bg-[#0f172a] border-b border-slate-800 px-4 sm:px-6 py-2.5 flex items-center justify-between shrink-0 w-full">
        {/* Left Info & Problems link */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => navigate('/problems')}
            className="flex items-center gap-1 text-slate-400 hover:text-white bg-slate-900 border border-slate-800 rounded-lg px-2.5 py-1 text-xs font-semibold transition-all cursor-pointer"
            title="Return to Problem List"
          >
            <ListFilter className="size-3.5" />
            <span className="hidden sm:inline">Problems</span>
          </button>

          <span className={`px-2.5 py-0.5 rounded text-[10px] font-bold border uppercase tracking-wider ${
            question.difficulty === 'easy' ? 'border-emerald-500/20 text-emerald-400 bg-emerald-950/20' :
            question.difficulty === 'medium' ? 'border-amber-500/20 text-amber-400 bg-amber-950/20' :
            'border-rose-500/20 text-rose-400 bg-rose-950/20'
          }`}>
            {question.difficulty}
          </span>
          <h2 className="text-sm font-bold text-white tracking-tight truncate max-w-xs md:max-w-md">
            {question.title}
          </h2>

          {/* Interactive Language Selector in Header */}
          <div className="flex items-center bg-slate-900 border border-slate-800 rounded-lg p-0.5">
            {(['c', 'cpp', 'java'] as Language[]).map((lang) => (
              <button
                key={lang}
                onClick={() => handleLanguageChange(lang)}
                className={`px-2 py-0.5 text-[10px] font-bold uppercase rounded transition-all cursor-pointer ${
                  selectedLanguage === lang
                    ? 'bg-indigo-600 text-white shadow-sm'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                {lang === 'cpp' ? 'C++' : lang.toUpperCase()}
              </button>
            ))}
          </div>

          <span className="hidden md:inline-block text-[11px] text-indigo-400 bg-indigo-950/30 border border-indigo-900/40 px-2 py-0.5 rounded-full capitalize">
            {question.topic}
          </span>
        </div>

        {/* Center: 4-Step Interactive Workflow Indicator */}
        <div className="hidden xl:flex items-center gap-1 bg-slate-900 border border-slate-800 rounded-full px-3 py-1">
          {[
            { id: 'review', label: '1. Review' },
            { id: 'identify', label: '2. Identify' },
            { id: 'fix', label: '3. Fix' },
            { id: 'validate', label: '4. Validate' }
          ].map((step) => (
            <Fragment key={step.id}>
              <button 
                onClick={() => {
                  setActiveStep(step.id as any);
                  if (step.id === 'identify') setActivePanel('identify');
                  if (step.id === 'validate') setActivePanel('tests');
                }}
                className={`text-[10px] font-semibold px-2.5 py-0.5 rounded-full transition-all cursor-pointer ${
                  activeStep === step.id
                    ? 'bg-indigo-600 text-white shadow-[0_0_10px_rgba(99,102,241,0.3)]'
                    : 'text-slate-500 hover:text-slate-300'
                }`}
              >
                {step.label}
              </button>
              {step.id !== 'validate' && <span className="text-slate-700 text-xs font-bold select-none">→</span>}
            </Fragment>
          ))}
        </div>

        {/* Right Controls: Timer, Next, Submit */}
        <div className="flex items-center gap-2.5">
          {/* Timer Display */}
          <div className={`flex items-center gap-2 font-mono text-xs border rounded-lg py-1.5 px-3 ${
            sessionMode === 'exam' 
              ? 'text-rose-400 bg-rose-950/20 border-rose-900/30 font-bold' 
              : 'text-slate-400 bg-slate-900/40 border-slate-800'
          }`}>
            <Clock className="size-3.5" />
            <span>
              {sessionMode === 'exam' 
                ? `${Math.floor(timeLeft / 60).toString().padStart(2, '0')}:${(timeLeft % 60).toString().padStart(2, '0')}`
                : `${Math.floor(elapsedSeconds / 60).toString().padStart(2, '0')}:${(elapsedSeconds % 60).toString().padStart(2, '0')}`
              }
            </span>
          </div>

          {/* Next Question Button */}
          <button
            onClick={handleNextQuestion}
            disabled={isFetchingNext}
            title="Fetch another challenge"
            className="hidden sm:flex items-center gap-1 text-slate-400 hover:text-white bg-slate-900/60 hover:bg-slate-800 border border-slate-800 rounded-lg text-xs font-semibold py-1.5 px-3 transition-all disabled:opacity-50 cursor-pointer"
          >
            <Sparkles className="size-3 text-indigo-400" />
            <span>Next</span>
          </button>

          {/* Submit Solution Button */}
          <button
            onClick={() => setShowConfirmSubmit(true)}
            disabled={isSubmitting || isRunning}
            className="flex items-center gap-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs py-1.5 px-3.5 transition-all shadow-[0_0_12px_rgba(99,102,241,0.2)] disabled:opacity-50 cursor-pointer"
          >
            <Send className="size-3" /> Submit
          </button>
        </div>
      </div>

      {/* 2. Full-Screen Workspace Body (3-Panel Desktop Layout) */}
      <div className="flex-1 grid grid-cols-1 lg:grid-cols-12 overflow-hidden w-full">
        {/* Left Column: Problem Statement & Visual Diagrams (col-span-4) */}
        <div className="lg:col-span-4 border-r border-slate-800 flex flex-col overflow-y-auto p-5 space-y-5 bg-[#0a0e1a]/40">
          {/* Problem Description */}
          <div className="space-y-2">
            <h3 className="text-[11px] font-bold uppercase tracking-wider text-indigo-400 flex items-center gap-1.5">
              <Search className="size-3.5" /> Problem Description
            </h3>
            <div className="text-slate-300 text-xs leading-relaxed font-normal space-y-3">
              {question.problemStatement.split('\n\n').map((paragraph, index) => (
                <p key={index}>{paragraph}</p>
              ))}
            </div>
          </div>

          <div className="border-t border-slate-800/80"></div>

          {/* Visible Examples */}
          <div className="space-y-4">
            <h3 className="text-[11px] font-bold uppercase tracking-wider text-slate-400">Examples</h3>
            {question.visibleTestCases.map((testCase, index) => {
              const isVisualTopic = ['trees', 'graphs', '2ddp', 'matrix-dp'].includes(question.topic) || 
                                    ['tree', 'graph', 'matrix', 'linkedList'].includes(testCase.visualData?.type || '');
              const shouldShowDiagram = isVisualTopic && testCase.visualData;

              return (
                <div key={index} className="space-y-2">
                  <h4 className="text-xs font-bold text-white tracking-wide">
                    Example {index + 1}:
                  </h4>

                  <div className="bg-[#0f172a]/90 border border-slate-800/90 rounded-xl p-3.5 space-y-3 font-sans text-xs">
                    {/* Input */}
                    <div className="space-y-1">
                      <div className="text-[11px] font-bold text-slate-400">Input:</div>
                      <pre className="p-2.5 bg-[#080c14] border border-slate-800/80 rounded-lg font-mono text-xs text-indigo-200 overflow-x-auto whitespace-pre">
                        {testCase.input}
                      </pre>
                    </div>

                    {/* Diagram placed below the relevant Input */}
                    {shouldShowDiagram && (
                      <div className="pt-0.5">
                        <VisualDiagram visualData={testCase.visualData} className="mt-1" />
                      </div>
                    )}

                    {/* Output */}
                    <div className="space-y-1">
                      <div className="text-[11px] font-bold text-slate-400">Output:</div>
                      <pre className="p-2.5 bg-[#080c14] border border-slate-800/80 rounded-lg font-mono text-xs text-emerald-300 overflow-x-auto whitespace-pre">
                        {testCase.expectedOutput}
                      </pre>
                    </div>

                    {/* Explanation */}
                    {testCase.explanation && (
                      <div className="space-y-1 pt-1.5 border-t border-slate-800/60">
                        <div className="text-[11px] font-bold text-slate-400">Explanation:</div>
                        <p className="text-slate-300 text-xs leading-relaxed">
                          {testCase.explanation}
                        </p>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>

          <div className="border-t border-slate-800/80"></div>

          {/* Constraints */}
          <div className="space-y-2">
            <h3 className="text-[11px] font-bold uppercase tracking-wider text-slate-400">Constraints</h3>
            <ul className="list-disc pl-4 text-slate-400 text-xs leading-relaxed space-y-1">
              {question.constraints.map((c, i) => (
                <li key={i}>{c}</li>
              ))}
            </ul>
          </div>

          <div className="border-t border-slate-800/80"></div>

          {/* Target Complexity */}
          <div className="space-y-2">
            <h3 className="text-[11px] font-bold uppercase tracking-wider text-slate-400">Target Complexity</h3>
            <div className="flex gap-4 text-xs bg-slate-900/50 border border-slate-800 rounded-xl p-3">
              <div>
                <span className="text-[10px] text-slate-500 font-semibold block uppercase">Time</span>
                <span className="font-mono text-white text-xs font-bold">{question.expectedComplexity.time}</span>
              </div>
              <div className="border-r border-slate-800"></div>
              <div>
                <span className="text-[10px] text-slate-500 font-semibold block uppercase">Space</span>
                <span className="font-mono text-white text-xs font-bold">{question.expectedComplexity.space}</span>
              </div>
            </div>
          </div>
        </div>

        {/* Center Column: Monaco Code Editor (col-span-5) */}
        <div className="lg:col-span-5 border-r border-slate-800 flex flex-col overflow-hidden relative">
          {/* Editor Header Bar */}
          <div className="bg-[#0f172a]/80 border-b border-slate-800/80 px-4 py-2 flex items-center justify-between shrink-0">
            <div className="flex items-center gap-2">
              <span className="text-xs font-semibold text-slate-300 uppercase tracking-wider">Buggy Code Editor</span>
              
              {/* Language Selector Buttons */}
              <div className="flex items-center bg-slate-950 border border-slate-800 rounded-md p-0.5 ml-2">
                {(['c', 'cpp', 'java'] as Language[]).map((lang) => (
                  <button
                    key={lang}
                    onClick={() => handleLanguageChange(lang)}
                    className={`px-2 py-0.5 text-[10px] font-bold uppercase rounded transition-all cursor-pointer ${
                      selectedLanguage === lang
                        ? 'bg-indigo-600 text-white'
                        : 'text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    {lang === 'cpp' ? 'C++' : lang.toUpperCase()}
                  </button>
                ))}
              </div>
            </div>
            <button 
              onClick={handleResetCode}
              className="flex items-center gap-1 py-1 px-2.5 hover:bg-slate-800 rounded text-slate-400 hover:text-white transition-colors text-[11px] cursor-pointer"
              title="Reset Code to Initial Buggy State"
            >
              <RotateCcw className="size-3" />
              <span>Reset</span>
            </button>
          </div>

          {/* Monaco Editor */}
          <div className="flex-1 w-full bg-[#1e293b]/10">
            <Editor
              height="100%"
              language={selectedLanguage === 'cpp' ? 'cpp' : selectedLanguage === 'java' ? 'java' : 'c'}
              value={code}
              onChange={(value) => {
                setCode(value || '');
                if (activeStep === 'review' || activeStep === 'identify') {
                  setActiveStep('fix');
                }
              }}
              theme="vs-dark"
              options={{
                fontSize: Number(localStorage.getItem('editor_font_size')) || 14,
                minimap: { enabled: localStorage.getItem('editor_minimap') === 'true' },
                wordWrap: localStorage.getItem('editor_word_wrap') === 'false' ? 'off' : 'on',
                tabSize: Number(localStorage.getItem('editor_tab_size')) || 4,
                scrollbar: {
                  vertical: 'visible',
                  horizontal: 'visible',
                  verticalScrollbarSize: 8,
                  horizontalScrollbarSize: 8,
                },
                lineNumbersMinChars: 3,
                automaticLayout: true,
                padding: { top: 10 },
              }}
            />
          </div>

          {/* Editor Footer Action Bar */}
          <div className="border-t border-slate-800 p-3 bg-[#090d16] flex items-center justify-between shrink-0">
            <div className="text-xs text-slate-500 font-medium">
              Lines: {code.split('\n').length} • Active: <span className="text-indigo-400 font-semibold capitalize">{activeStep}</span>
            </div>
            <button
              onClick={handleRun}
              disabled={isRunning || isSubmitting}
              className="flex items-center gap-1.5 rounded-lg border border-indigo-500/40 bg-indigo-600/90 hover:bg-indigo-500 text-white font-bold text-xs py-2 px-5 transition-all shadow-[0_0_12px_rgba(99,102,241,0.2)] disabled:opacity-50 cursor-pointer"
            >
              {isRunning ? (
                <>
                  <span className="size-3 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
                  <span>Executing...</span>
                </>
              ) : (
                <>
                  <Play className="size-3 fill-white text-white" />
                  <span>Run Code</span>
                </>
              )}
            </button>
          </div>
        </div>


        {/* Right Column: Multi-tab Panel (col-span-3) */}
        <div className="lg:col-span-3 flex flex-col overflow-hidden bg-[#090d16]/30">
          {/* Tab Header */}
          <div className="bg-[#0f172a]/80 border-b border-slate-800/80 flex items-center shrink-0 overflow-x-auto">
            {[
              { id: 'tests', label: 'Tests', icon: CheckCircle2 },
              { id: 'identify', label: 'Identify', icon: BugIcon },
              { id: 'ai', label: 'AI Chat', icon: Bot },
              { id: 'history', label: 'Runs', icon: History },
              ...(sessionMode === 'practice' ? [{ id: 'hints', label: 'Hints', icon: HelpCircle }] : [])
            ].map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActivePanel(tab.id as any)}
                  className={`flex-1 min-w-[55px] flex items-center justify-center gap-1 py-2.5 text-[11px] font-bold border-b-2 transition-all cursor-pointer ${
                    activePanel === tab.id
                      ? 'border-indigo-500 text-white bg-slate-900/60'
                      : 'border-transparent text-slate-500 hover:text-slate-300'
                  }`}
                >
                  <Icon className="size-3" />
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </div>

          {/* Tab Contents */}
          {activePanel === 'ai' ? (
            <div className="flex-1 overflow-hidden">
              <AIAssistantPanel
                question={question}
                selectedLanguage={selectedLanguage}
                currentEditorCode={code}
                originalBuggyCode={originalBuggyCode}
                lastRunCode={lastRunCode}
                codeChangesDiff={computeCodeDiff(originalBuggyCode, code)}
                latestExecutionResult={latestExecutionResult}
                consoleLogs={consoleLogs}
                sessionMode={sessionMode}
                isSubmitted={isSubmitted}
                lastSubmittedCode={lastSubmittedCode}
                messages={chatMessages}
                onUpdateMessages={setChatMessages}
              />
            </div>
          ) : (
            <div className="flex-1 overflow-y-auto p-4">
              {/* 1. TEST CASES & EXECUTION RESULT TAB */}
              {activePanel === 'tests' && (
                <div className="space-y-4">
                  {/* Case selection tabs */}
                  <div className="flex items-center gap-2 overflow-x-auto pb-1">
                    {testCases.map((tc, index) => {
                      const isExecuted = tc.passed !== undefined;
                      return (
                        <button
                          key={tc.id}
                          onClick={() => setSelectedTestId(tc.id)}
                          className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold border transition-all cursor-pointer shrink-0 ${
                            selectedTestId === tc.id
                              ? 'border-indigo-500 bg-indigo-600/15 text-white shadow-sm'
                              : 'border-slate-800 bg-slate-900/50 text-slate-400 hover:text-slate-200 hover:border-slate-700'
                          }`}
                        >
                          {isExecuted ? (
                            tc.passed ? (
                              <CheckCircle2 className="size-3.5 text-emerald-400" />
                            ) : (
                              <XCircle className="size-3.5 text-rose-400" />
                            )
                          ) : (
                            <span className="size-1.5 rounded-full bg-slate-600"></span>
                          )}
                          <span>Test Case {index + 1}</span>
                        </button>
                      );
                    })}
                  </div>

                  {(() => {
                    const currentCase = testCases.find(t => t.id === selectedTestId) || testCases[0];
                    if (!currentCase) return null;
                    const caseIndex = testCases.findIndex(t => t.id === currentCase.id);
                    const isExecuted = currentCase.passed !== undefined;

                    return (
                      <div className="space-y-3.5">
                        {/* Compact Result Status Banner when executed */}
                        {isExecuted && (
                          <div className={`p-3 rounded-xl border flex items-center justify-between ${
                            currentCase.passed
                              ? 'bg-emerald-950/20 border-emerald-900/40 text-emerald-400'
                              : 'bg-rose-950/20 border-rose-900/40 text-rose-400'
                          }`}>
                            <div className="font-bold text-xs">
                              Test Case {caseIndex + 1}
                            </div>
                            <div className="flex items-center gap-1.5 text-xs font-bold">
                              {currentCase.passed ? (
                                <>
                                  <CheckCircle2 className="size-4 text-emerald-400" />
                                  <span>Passed</span>
                                </>
                              ) : (
                                <>
                                  <XCircle className="size-4 text-rose-400" />
                                  <span>Failed</span>
                                </>
                              )}
                            </div>
                          </div>
                        )}

                        {/* Input */}
                        <div className="space-y-1">
                          <div className="text-[11px] font-semibold text-slate-400">Input:</div>
                          <pre className="p-2.5 bg-[#0a0e17] border border-slate-800 rounded-lg font-mono text-xs text-slate-200 whitespace-pre overflow-x-auto">
                            {currentCase.input}
                          </pre>
                        </div>

                        {/* Expected Output */}
                        <div className="space-y-1">
                          <div className="text-[11px] font-semibold text-slate-400">
                            {isExecuted ? 'Expected:' : 'Expected Output:'}
                          </div>
                          <pre className="p-2.5 bg-[#0a0e17] border border-slate-800 rounded-lg font-mono text-xs text-emerald-300 overflow-x-auto">
                            {currentCase.expectedOutput}
                          </pre>
                        </div>

                        {/* Output (only when executed) */}
                        {isExecuted && (
                          <div className="space-y-1">
                            <div className="text-[11px] font-semibold text-slate-400">Output:</div>
                            <pre className={`p-2.5 border rounded-lg font-mono text-xs overflow-x-auto ${
                              currentCase.passed
                                ? 'bg-emerald-950/15 border-emerald-900/40 text-emerald-300'
                                : 'bg-rose-950/15 border-rose-900/40 text-rose-300'
                            }`}>
                              {currentCase.actualOutput || 'No output produced'}
                            </pre>
                          </div>
                        )}
                      </div>
                    );
                  })()}
                </div>
              )}

            {/* 2. IDENTIFY BUG TAB (Step 2 in workflow) */}
            {activePanel === 'identify' && (
              <div className="space-y-4">
                <div className="space-y-1">
                  <h4 className="text-xs font-bold text-white flex items-center gap-1.5">
                    <BugIcon className="size-3.5 text-amber-400" />
                    <span>Bug Diagnosis (Step 2)</span>
                  </h4>
                  <p className="text-[11px] text-slate-400 leading-relaxed">
                    Diagnose the cause of the bug before editing. A correct diagnosis adds +20 points to your assessment score.
                  </p>
                </div>

                <div className="space-y-2">
                  <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
                    Suspected Bug Category
                  </label>
                  <select
                    value={userDiagnosis.bugType}
                    disabled={userDiagnosis.isLocked}
                    onChange={(e) => setUserDiagnosis(prev => ({ ...prev, bugType: e.target.value as BugType }))}
                    className="w-full bg-[#0f172a] border border-slate-800 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-indigo-500"
                  >
                    <option value="">-- Select suspected bug type --</option>
                    {BUG_TYPES.map(type => (
                      <option key={type} value={type}>{type}</option>
                    ))}
                  </select>
                </div>

                <div className="space-y-2">
                  <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
                    Diagnosis Reasoning
                  </label>
                  <textarea
                    rows={4}
                    value={userDiagnosis.notes}
                    disabled={userDiagnosis.isLocked}
                    onChange={(e) => setUserDiagnosis(prev => ({ ...prev, notes: e.target.value }))}
                    placeholder="Describe what logic/line is failing and why..."
                    className="w-full bg-[#0f172a] border border-slate-800 rounded-xl p-3 text-xs text-slate-200 placeholder-slate-600 focus:outline-none focus:border-indigo-500 resize-none font-mono"
                  />
                </div>

                <button
                  onClick={() => {
                    setUserDiagnosis(prev => ({ ...prev, isLocked: !prev.isLocked }));
                    if (!userDiagnosis.isLocked) {
                      setActiveStep('fix');
                    }
                  }}
                  className={`w-full py-2.5 rounded-xl font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer ${
                    userDiagnosis.isLocked
                      ? 'bg-amber-950/30 border border-amber-500/30 text-amber-300 hover:bg-amber-900/30'
                      : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-[0_0_12px_rgba(99,102,241,0.25)]'
                  }`}
                >
                  {userDiagnosis.isLocked ? (
                    <><span>Unlock to Edit</span></>
                  ) : (
                    <><span>Confirm Diagnosis & Proceed to Fix</span> <ArrowRight className="size-3.5" /></>
                  )}
                </button>
              </div>
            )}



            {/* 4. RUN HISTORY TAB */}
            {activePanel === 'history' && (
              <div className="space-y-3">
                <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
                  Execution History ({runHistory.length})
                </div>
                {runHistory.length === 0 ? (
                  <p className="text-xs text-slate-500 py-6 text-center">No runs executed yet in this session.</p>
                ) : (
                  runHistory.map((item, idx) => (
                    <div key={item.id} className="bg-slate-900/50 border border-slate-800 rounded-xl p-3 space-y-1.5">
                      <div className="flex items-center justify-between text-xs">
                        <span className="font-bold text-white flex items-center gap-1.5">
                          {item.passed ? <CheckCircle2 className="size-3.5 text-emerald-400" /> : <XCircle className="size-3.5 text-rose-400" />}
                          Run #{runHistory.length - idx}
                        </span>
                        <span className="text-[10px] text-slate-500 font-mono">{item.timestamp}</span>
                      </div>
                      <div className="text-[11px] text-slate-400">
                        Passed: <span className={item.passed ? 'text-emerald-400 font-bold' : 'text-rose-400 font-bold'}>{item.passedCount}/{item.totalCount}</span> • Time: {item.executionTimeMs}ms
                      </div>
                    </div>
                  ))
                )}
              </div>
            )}

            {/* 5. HINTS TAB (Practice mode only) */}
            {activePanel === 'hints' && (
              <div className="space-y-4">
                <p className="text-slate-400 text-xs leading-relaxed">
                  Need guidance? Request a conceptual hint. Each hint requested will deduct 5% from your final score.
                </p>

                {hintsUsed >= 1 && (
                  <div className="bg-[#111827] border border-slate-800 rounded-xl p-3.5 space-y-1">
                    <h4 className="text-xs font-bold text-indigo-400">Hint 1: Intended Strategy</h4>
                    <p className="text-xs text-slate-300 leading-relaxed">
                      {question.intendedApproach || 'Examine the core invariants, base conditions, and state transitions of this algorithm.'}
                    </p>
                  </div>
                )}

                {hintsUsed >= 2 && (
                  <div className="bg-[#111827] border border-slate-800 rounded-xl p-3.5 space-y-1">
                    <h4 className="text-xs font-bold text-indigo-400">Hint 2: Bug Clue</h4>
                    <p className="text-xs text-slate-300 leading-relaxed">
                      {`Look closely at loop boundaries, base cases, visited state tracking, or edge-case initializations in this ${selectedLanguage.toUpperCase()} code.`}
                    </p>
                  </div>
                )}

                {hintsUsed < 2 ? (
                  <button
                    onClick={() => setHintsUsed(prev => prev + 1)}
                    className="w-full py-2.5 rounded-xl border border-indigo-500/30 bg-indigo-500/10 text-indigo-400 font-semibold text-xs hover:bg-indigo-500/20 transition-all cursor-pointer"
                  >
                    Request Hint #{hintsUsed + 1}
                  </button>
                ) : (
                  <div className="text-center py-2 text-[10px] text-slate-500">
                    All hints utilized. Fix the bug to proceed.
                  </div>
                )}
              </div>
            )}
          </div>
          )}
        </div>
      </div>

      {/* 3. Confirm Submit Modal */}
      {showConfirmSubmit && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm">
          <div className="bg-[#111827] border border-slate-800 w-full max-w-md rounded-2xl p-6 space-y-4 shadow-2xl relative">
            <button 
              onClick={() => setShowConfirmSubmit(false)}
              className="absolute top-4 right-4 text-slate-400 hover:text-white cursor-pointer"
            >
              <X className="size-4" />
            </button>

            <div className="space-y-2">
              <h3 className="text-lg font-bold text-white tracking-tight">Confirm Submission</h3>
              <p className="text-slate-400 text-xs leading-relaxed">
                Submitting will execute all hidden validation test cases and evaluate your bug diagnosis.
              </p>
            </div>

            {/* Diagnosis summary check */}
            <div className="bg-slate-900 border border-slate-800 rounded-xl p-3 text-xs space-y-1.5">
              <div className="text-slate-400">
                <span className="font-semibold text-slate-300">Diagnosed Bug:</span>{' '}
                {userDiagnosis.bugType ? (
                  <span className="text-indigo-400 font-bold uppercase">{userDiagnosis.bugType}</span>
                ) : (
                  <span className="text-amber-400 italic">None selected</span>
                )}
              </div>
              <div className="text-slate-400">
                <span className="font-semibold text-slate-300">Diagnosis Notes:</span>{' '}
                {userDiagnosis.notes.trim() ? (
                  <span className="text-slate-300">"{userDiagnosis.notes.slice(0, 50)}..."</span>
                ) : (
                  <span className="text-amber-400 italic">No notes written</span>
                )}
              </div>
            </div>

            <div className="flex gap-3 justify-end pt-2">
              <button
                onClick={() => setShowConfirmSubmit(false)}
                className="px-4 py-2 border border-slate-700 bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs rounded-lg transition-all cursor-pointer"
              >
                Cancel
              </button>
              <button
                onClick={() => submitCode(false)}
                disabled={isSubmitting}
                className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs rounded-lg transition-all shadow-[0_0_12px_rgba(99,102,241,0.3)] disabled:opacity-50 cursor-pointer"
              >
                {isSubmitting ? 'Evaluating...' : 'Confirm Submit'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 4. Warnings overlay (Timer) */}
      {timerWarning && (
        <div className="fixed bottom-6 right-6 z-50 bg-[#161e31] border border-amber-500/30 text-amber-400 rounded-xl p-4 flex items-center justify-between gap-4 shadow-2xl animate-bounce">
          <div className="flex items-center gap-2 text-xs font-semibold">
            <Clock className="size-4 text-amber-500 shrink-0" />
            <span>{timerWarning}</span>
          </div>
          <button 
            onClick={() => setTimerWarning(null)}
            className="text-slate-400 hover:text-white cursor-pointer"
          >
            <X className="size-3" />
          </button>
        </div>
      )}
    </div>
  );
}
