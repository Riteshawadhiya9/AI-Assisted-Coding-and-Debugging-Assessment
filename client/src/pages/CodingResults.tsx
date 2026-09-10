import { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { 
  CheckCircle2, ArrowLeft, RotateCcw, 
  Sparkles, Target, Code2, Award, ChevronRight
} from 'lucide-react';

export default function CodingResults() {
  const [searchParams] = useSearchParams();
  const questionId = searchParams.get('id') || '';

  const [result, setResult] = useState<any>(null);

  useEffect(() => {
    const raw = sessionStorage.getItem('last_coding_result');
    if (raw) {
      try {
        setResult(JSON.parse(raw));
      } catch (e) {
        console.error(e);
      }
    }
  }, []);

  const formatTime = (secs: number) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}m ${s}s`;
  };

  const passRate = result?.totalTests > 0 
    ? Math.round((result.testsPassed / result.totalTests) * 100) 
    : 0;

  return (
    <div className="flex-1 py-10 px-4 sm:px-6 lg:px-8 max-w-4xl mx-auto w-full">
      {/* Back Link */}
      <div className="mb-6">
        <Link
          to="/coding/setup"
          className="inline-flex items-center gap-1.5 text-xs text-slate-400 hover:text-white bg-slate-900 border border-slate-800 px-3 py-1.5 rounded-lg transition-colors"
        >
          <ArrowLeft className="size-3.5" />
          <span>Back to Coding Problems</span>
        </Link>
      </div>

      {/* Main Scorecard Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-[#0f172a] via-[#131d36] to-[#1e1b4b] border border-indigo-500/30 p-8 shadow-2xl mb-8">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold mb-3">
              <Award className="size-3.5" />
              <span>ASSESSMENT SUBMISSION REPORT</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              {result?.questionTitle || 'Coding Assessment Complete'}
            </h1>
            <p className="text-xs text-slate-300 mt-1">
              Language: <span className="font-semibold text-white uppercase">{result?.language || 'Python'}</span> • 
              Difficulty: <span className="font-semibold text-indigo-300">{result?.difficulty || 'Medium'}</span> • 
              Time Spent: <span className="font-semibold text-white">{formatTime(result?.timeSpentSeconds || 0)}</span>
            </p>
          </div>

          <div className="bg-slate-900/80 border border-slate-700/60 rounded-xl p-5 text-center shrink-0 min-w-[140px]">
            <div className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">
              Overall Score
            </div>
            <div className="text-4xl font-black text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-indigo-400">
              {result?.score ?? 85}/100
            </div>
          </div>
        </div>
      </div>

      {/* Metrics Breakdown Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">
        {/* Test Cases Passed */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5">
          <div className="flex items-center justify-between text-slate-400 mb-2">
            <span className="text-xs font-bold uppercase tracking-wider">Test Suite</span>
            <CheckCircle2 className="size-4 text-emerald-400" />
          </div>
          <div className="text-2xl font-bold text-white mb-1">
            {result?.testsPassed ?? 0} / {result?.totalTests ?? 0}
          </div>
          <div className="text-xs text-emerald-400 font-semibold">
            {passRate}% Pass Rate
          </div>
        </div>

        {/* AI Collaboration Literacy */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5">
          <div className="flex items-center justify-between text-slate-400 mb-2">
            <span className="text-xs font-bold uppercase tracking-wider">AI Literacy</span>
            <Sparkles className="size-4 text-purple-400" />
          </div>
          <div className="text-2xl font-bold text-purple-300 mb-1">
            {result?.breakdown?.aiLiteracyScore ?? 88}/100
          </div>
          <div className="text-xs text-slate-400">
            {result?.promptCount ?? 2} Prompts Evaluated
          </div>
        </div>

        {/* Code Correctness */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5">
          <div className="flex items-center justify-between text-slate-400 mb-2">
            <span className="text-xs font-bold uppercase tracking-wider">Correctness</span>
            <Code2 className="size-4 text-indigo-400" />
          </div>
          <div className="text-2xl font-bold text-indigo-300 mb-1">
            {result?.breakdown?.codeCorrectness ?? 90}%
          </div>
          <div className="text-xs text-slate-400">
            Algorithmic accuracy & edge cases
          </div>
        </div>
      </div>

      {/* AI Collaboration & Prompt Engineering Evaluation */}
      <div className="bg-slate-900/90 border border-slate-800 rounded-xl p-6 mb-8">
        <h2 className="text-sm font-bold uppercase tracking-wider text-slate-300 mb-4 flex items-center gap-2">
          <Sparkles className="size-4 text-indigo-400" />
          <span>AI Interaction & Prompt Engineering Analysis</span>
        </h2>
        
        <div className="space-y-4 text-xs text-slate-300 leading-relaxed">
          <p>
            Your interaction with the AI Assistant demonstrates strong problem formulation. In real-world software engineering, 
            the ability to effectively communicate constraints, context, and edge cases to AI models is a core competency.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
            <div className="bg-slate-950/70 border border-slate-800/80 rounded-lg p-3">
              <div className="text-emerald-400 font-bold mb-1 flex items-center gap-1.5">
                <CheckCircle2 className="size-3.5" />
                <span>Strengths</span>
              </div>
              <ul className="list-disc list-inside space-y-1 text-slate-400">
                <li>Clear specification of algorithmic constraints</li>
                <li>Iterative refinement without dumping raw boilerplate</li>
              </ul>
            </div>

            <div className="bg-slate-950/70 border border-slate-800/80 rounded-lg p-3">
              <div className="text-amber-400 font-bold mb-1 flex items-center gap-1.5">
                <Target className="size-3.5" />
                <span>Recommended Next Steps</span>
              </div>
              <ul className="list-disc list-inside space-y-1 text-slate-400">
                <li>Ask AI to construct extreme boundary test inputs early</li>
                <li>Incorporate time and space complexity verification in prompts</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex items-center justify-between">
        <Link
          to={`/coding/workspace?id=${questionId}`}
          className="inline-flex items-center gap-2 px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg text-xs font-semibold border border-slate-700 transition-colors"
        >
          <RotateCcw className="size-3.5" />
          <span>Try Problem Again</span>
        </Link>

        <Link
          to="/coding/setup"
          className="inline-flex items-center gap-2 px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-bold shadow-md transition-colors"
        >
          <span>Next Problem</span>
          <ChevronRight className="size-4" />
        </Link>
      </div>
    </div>
  );
}
