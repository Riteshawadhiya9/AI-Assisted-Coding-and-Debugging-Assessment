import { useEffect, useState } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import { 
  CheckCircle2, XCircle, AlertTriangle, BookOpen, 
  RotateCcw, ArrowRight, Bug, Target, LayoutDashboard, Sparkles
} from 'lucide-react';
import type { Attempt, Question } from '../types';

export default function Results() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const attemptId = searchParams.get('attemptId');

  const [attempt, setAttempt] = useState<Attempt | null>(null);
  const [question, setQuestion] = useState<Question | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [isFetchingNext, setIsFetchingNext] = useState<boolean>(false);

  useEffect(() => {
    async function loadAttemptData() {
      try {
        const localAttempts = localStorage.getItem('debuglab_attempts');
        if (!localAttempts) throw new Error('No attempts found');
        
        const parsed: Attempt[] = JSON.parse(localAttempts);
        const currentAttempt = parsed.find(a => a.id === attemptId);
        if (!currentAttempt) throw new Error('Attempt not found');
        
        setAttempt(currentAttempt);

        // Fetch question details for explanations
        const res = await fetch(`/api/questions/${currentAttempt.questionId}/solution`);
        if (res.ok) {
          const qData = await res.json();
          setQuestion(qData);
        }
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }
    if (attemptId) {
      loadAttemptData();
    }
  }, [attemptId]);

  const handleNextChallenge = async () => {
    if (!attempt || isFetchingNext) return;
    setIsFetchingNext(true);
    try {
      const res = await fetch(`/api/questions/random?topic=${attempt.topic}&language=${attempt.language}`);
      if (res.ok) {
        const nextQ = await res.json();
        navigate(`/workspace?id=${nextQ.id}&mode=${attempt.mode}`);
      } else {
        const anyRes = await fetch('/api/questions/random');
        if (anyRes.ok) {
          const nextAny = await anyRes.json();
          navigate(`/workspace?id=${nextAny.id}&mode=${attempt.mode}`);
        }
      }
    } catch (err) {
      console.error(err);
      navigate('/setup');
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
          <p className="text-sm font-semibold">Analyzing your debugging assessment...</p>
        </div>
      </div>
    );
  }

  if (!attempt || !question) {
    return (
      <div className="flex h-[80vh] items-center justify-center text-rose-400 p-6">
        <div className="text-center space-y-4 max-w-md">
          <AlertTriangle className="size-12 mx-auto text-rose-500" />
          <h2 className="text-lg font-bold text-white">Results Unavailable</h2>
          <p className="text-sm text-slate-400">The requested attempt results could not be located in local storage.</p>
          <button 
            onClick={() => navigate('/')}
            className="px-4 py-2 bg-indigo-600 rounded-lg text-white font-semibold text-xs hover:bg-indigo-500"
          >
            Return to Dashboard
          </button>
        </div>
      </div>
    );
  }

  const isPassed = attempt.status === 'passed';

  return (
    <div className="mx-auto max-w-[960px] px-6 py-10 relative z-10 space-y-8">
      {/* Page Title */}
      <div className="space-y-1.5 text-center">
        <h1 className="text-3xl font-black tracking-tight text-white">Assessment Report</h1>
        <p className="text-slate-400 text-xs font-medium">Review your scoring breakdown, test results, and algorithmic analysis below.</p>
      </div>

      {/* Main Scorecard card */}
      <div className={`border rounded-2xl p-6 md:p-8 flex flex-col md:flex-row items-center justify-between gap-6 relative overflow-hidden backdrop-blur-md ${
        isPassed 
          ? 'border-emerald-500/25 bg-emerald-500/[0.03] shadow-[0_0_30px_rgba(16,185,129,0.05)]' 
          : 'border-rose-500/25 bg-rose-500/[0.03] shadow-[0_0_30px_rgba(244,63,94,0.05)]'
      }`}>
        <div className="flex items-center gap-4 text-center md:text-left flex-col md:flex-row">
          {isPassed ? (
            <CheckCircle2 className="size-14 text-emerald-400 shrink-0" />
          ) : (
            <XCircle className="size-14 text-rose-400 shrink-0" />
          )}
          <div className="space-y-1">
            <h2 className="text-xl font-bold text-white">
              {isPassed ? 'Algorithmic Bug Resolved!' : 'Submission Incomplete'}
            </h2>
            <p className="text-slate-400 text-xs">
              Topic: <span className="uppercase font-semibold text-slate-300">{attempt.topic}</span> • 
              Difficulty: <span className="capitalize font-semibold text-slate-300">{attempt.difficulty}</span> • 
              Language: <span className="uppercase font-semibold text-slate-300">{attempt.language}</span>
            </p>
          </div>
        </div>

        {/* Stats segment */}
        <div className="flex items-center gap-6 shrink-0 bg-slate-900/60 border border-slate-800 rounded-xl py-3.5 px-6">
          <div className="text-center">
            <span className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">Total Score</span>
            <div className={`text-2xl font-black mt-0.5 ${isPassed ? 'text-emerald-400' : 'text-rose-400'}`}>
              {attempt.score}%
            </div>
          </div>
          <div className="h-8 w-px bg-slate-800"></div>
          <div className="text-center">
            <span className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">Time</span>
            <div className="text-2xl font-black text-white mt-0.5">
              {Math.floor(attempt.timeSpentSeconds / 60)}m {attempt.timeSpentSeconds % 60}s
            </div>
          </div>
          <div className="h-8 w-px bg-slate-800"></div>
          <div className="text-center">
            <span className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">Tests Passed</span>
            <div className="text-2xl font-black text-white mt-0.5">
              {attempt.testsPassed} / {attempt.totalTests}
            </div>
          </div>
        </div>
      </div>

      {/* Score Breakdown Details */}
      {attempt.scoreBreakdown && (
        <div className="bg-[#0f172a]/60 border border-slate-800 rounded-2xl p-6 space-y-4">
          <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-2">
            <Target className="size-4 text-indigo-400" /> Score Breakdown
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div className="bg-slate-900/50 border border-slate-800/80 rounded-xl p-3">
              <span className="text-[10px] text-slate-500 uppercase font-semibold block">Code Fix</span>
              <span className="text-sm font-bold text-white font-mono">+{attempt.scoreBreakdown.correctness} pts</span>
            </div>
            <div className="bg-slate-900/50 border border-slate-800/80 rounded-xl p-3">
              <span className="text-[10px] text-slate-500 uppercase font-semibold block">Test Coverage</span>
              <span className="text-sm font-bold text-white font-mono">+{attempt.scoreBreakdown.tests} pts</span>
            </div>
            <div className="bg-slate-900/50 border border-slate-800/80 rounded-xl p-3">
              <span className="text-[10px] text-slate-500 uppercase font-semibold block">Bug Diagnosis</span>
              <span className="text-sm font-bold text-white font-mono">+{attempt.scoreBreakdown.diagnosis} pts</span>
            </div>
            <div className="bg-slate-900/50 border border-slate-800/80 rounded-xl p-3">
              <span className="text-[10px] text-slate-500 uppercase font-semibold block">Time Efficiency</span>
              <span className="text-sm font-bold text-white font-mono">+{attempt.scoreBreakdown.timeBonus} pts</span>
            </div>
          </div>
        </div>
      )}

      {/* Diagnosis Comparison */}
      <div className="bg-[#0f172a]/60 border border-slate-800 rounded-2xl p-6 space-y-4">
        <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-2">
          <Bug className="size-4 text-amber-400" /> Bug Diagnosis Accuracy
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 space-y-2">
            <div className="text-[10px] font-bold uppercase tracking-wider text-slate-500">Your Diagnosis</div>
            <div className="text-xs">
              <span className="font-semibold text-slate-400">Suspected Type: </span>
              <span className="font-bold text-indigo-400 uppercase">
                {attempt.diagnosedBugType || 'None specified'}
              </span>
            </div>
            <p className="text-xs text-slate-300 font-mono bg-slate-950 p-2.5 rounded-lg border border-slate-850">
              {attempt.diagnosisNotes || 'No diagnosis notes provided.'}
            </p>
          </div>

          <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 space-y-2">
            <div className="text-[10px] font-bold uppercase tracking-wider text-slate-500">Ground Truth Primary Bug</div>
            <div className="text-xs">
              <span className="font-semibold text-slate-400">Actual Category: </span>
              <span className="font-bold text-emerald-400 uppercase">
                {question.primaryBugType || 'LOGICAL'}
              </span>
            </div>
            <p className="text-xs text-slate-300 font-mono bg-slate-950 p-2.5 rounded-lg border border-slate-850">
              {question.explanation || 'Refer to problem notes.'}
            </p>
          </div>
        </div>
      </div>

      {/* Action panel */}
      <div className="flex flex-wrap gap-4 items-center justify-between">
        <div className="flex gap-3">
          <button
            onClick={() => navigate(`/workspace?id=${attempt.questionId}&mode=${attempt.mode}`)}
            className="flex items-center gap-1.5 rounded-xl border border-slate-700 bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs py-3 px-5 transition-all"
          >
            <RotateCcw className="size-3.5" /> Retry Question
          </button>
          <button
            onClick={() => navigate('/progress')}
            className="flex items-center gap-1.5 rounded-xl border border-slate-700 bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs py-3 px-5 transition-all"
          >
            <LayoutDashboard className="size-3.5" /> View All Progress
          </button>
        </div>

        <button
          onClick={handleNextChallenge}
          disabled={isFetchingNext}
          className="flex items-center gap-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs py-3 px-6 transition-all hover:shadow-[0_0_20px_rgba(99,102,241,0.4)] disabled:opacity-50"
        >
          <Sparkles className="size-3.5" />
          <span>{isFetchingNext ? 'Loading...' : 'Next Challenge'}</span>
          <ArrowRight className="size-3.5" />
        </button>
      </div>

      {/* Deep code bug explanation */}
      <div className="bg-[#111827]/50 border border-slate-800 rounded-2xl p-6 md:p-8 space-y-6">
        <h3 className="text-lg font-bold text-white tracking-tight flex items-center gap-2">
          <BookOpen className="size-5 text-indigo-400" /> Algorithmic Solution & Explanation
        </h3>

        <div className="space-y-6 text-sm text-slate-300 leading-relaxed font-medium">
          {/* Intended solution */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500">Correct Algorithmic Approach</h4>
            <p className="text-xs text-slate-300">{question.intendedApproach}</p>
          </div>

          <div className="border-t border-slate-800 my-2"></div>

          {/* Constraints and Complexity */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-2">
              <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500">Constraints & Edge Cases</h4>
              <ul className="list-disc pl-4 text-xs text-slate-400 space-y-1">
                {question.constraints.map((c, i) => (
                  <li key={i}>{c}</li>
                ))}
              </ul>
            </div>

            <div className="space-y-2">
              <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500">Expected Complexity</h4>
              <div className="flex gap-6 text-xs bg-slate-900/50 border border-slate-800 rounded-xl p-4">
                <div>
                  <span className="text-slate-500 font-semibold block mb-0.5 text-[10px] uppercase">Time</span>
                  <span className="font-mono text-white text-sm font-bold">{question.expectedComplexity.time}</span>
                </div>
                <div className="h-8 w-px bg-slate-800"></div>
                <div>
                  <span className="text-slate-500 font-semibold block mb-0.5 text-[10px] uppercase">Space</span>
                  <span className="font-mono text-white text-sm font-bold">{question.expectedComplexity.space}</span>
                </div>
              </div>
            </div>
          </div>

          <div className="border-t border-slate-800 my-2"></div>

          {/* Side-by-side or comparison details */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-2">
              <h4 className="text-xs font-bold uppercase tracking-wider text-rose-400">Initial Buggy Code</h4>
              <pre className="p-4 bg-slate-900 border border-slate-800 rounded-xl font-mono text-[11px] text-rose-300 overflow-x-auto leading-relaxed max-h-72">
                {question.buggyCode}
              </pre>
            </div>
            <div className="space-y-2">
              <h4 className="text-xs font-bold uppercase tracking-wider text-emerald-400">Correct Fixed Code</h4>
              <pre className="p-4 bg-slate-900 border border-slate-800 rounded-xl font-mono text-[11px] text-emerald-300 overflow-x-auto leading-relaxed max-h-72">
                {question.correctCode}
              </pre>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
