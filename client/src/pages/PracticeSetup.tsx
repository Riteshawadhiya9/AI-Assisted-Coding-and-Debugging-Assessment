import { useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { AlertCircle, ChevronRight } from 'lucide-react';
import type { Language, Topic, Difficulty } from '../types';

export default function PracticeSetup() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  // Settings states initialized from URL parameters
  const [language, setLanguage] = useState<Language>('cpp');
  const [topic, setTopic] = useState<Topic>(() => {
    const paramTopic = searchParams.get('topic') as Topic | null;
    return paramTopic && ['trees', 'graphs', '2ddp', 'advanced-dsa', 'random'].includes(paramTopic)
      ? paramTopic
      : 'random';
  });
  const [difficulty, setDifficulty] = useState<Difficulty>('medium');
  const [mode, setMode] = useState<'practice' | 'exam'>(() => {
    const paramMode = searchParams.get('mode');
    return paramMode === 'practice' || paramMode === 'exam' ? paramMode : 'practice';
  });
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleStart = async () => {
    setLoading(true);
    setError(null);
    try {
      // Build query string
      const query = new URLSearchParams();
      if (language) query.append('language', language);
      if (topic !== 'random') query.append('topic', topic);
      if (difficulty) query.append('difficulty', difficulty);

      const res = await fetch(`/api/questions/random?${query.toString()}`);
      if (!res.ok) {
        if (res.status === 404) {
          throw new Error('No question in the question bank matches your filters. Please try another language/topic combination.');
        } else {
          throw new Error('Server error retrieving question. Please try again.');
        }
      }

      const questionData = await res.json();
      // Redirect to the Workspace page with the question ID, mode, and language
      navigate(`/workspace?id=${questionData.id}&mode=${mode}&lang=${language}`);
    } catch (err: any) {
      setError(err.message || 'Failed to start session.');
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto max-w-[800px] px-6 py-10 relative z-10 space-y-8">
      {/* Title */}
      <div className="space-y-3 text-center">
        <h1 className="text-3xl font-black tracking-tight text-white">Configure Debugging Session</h1>
        <p className="text-slate-400 text-sm max-w-lg mx-auto">
          Tailor your debugging challenges by configuring the programming language, topic depth, and difficulty.
        </p>
      </div>

      <div className="bg-[#111827]/50 border border-slate-800 rounded-2xl p-6 md:p-8 space-y-6 backdrop-blur-md">
        {/* Error notification */}
        {error && (
          <div className="bg-rose-500/10 border border-rose-500/20 text-rose-400 rounded-xl p-4 flex items-start gap-3 text-sm">
            <AlertCircle className="size-5 shrink-0 mt-0.5" />
            <div>
              <span className="font-semibold">Selection Error:</span> {error}
            </div>
          </div>
        )}

        {/* 1. Language Toggle */}
        <div className="space-y-3">
          <label className="text-xs font-bold uppercase tracking-wider text-slate-400">Language</label>
          <div className="grid grid-cols-3 gap-3">
            {[
              { id: 'c', name: 'C', desc: 'Standard C' },
              { id: 'cpp', name: 'C++', desc: 'Modern C++' },
              { id: 'java', name: 'Java', desc: 'Java JDK 17' }
            ].map((lang) => (
              <button
                key={lang.id}
                onClick={() => setLanguage(lang.id as Language)}
                className={`flex flex-col items-center justify-center p-4 rounded-xl border text-center transition-all ${
                  language === lang.id
                    ? 'border-indigo-500 bg-indigo-500/10 text-white'
                    : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:border-slate-700'
                }`}
              >
                <span className="font-bold text-base">{lang.name}</span>
                <span className="text-[10px] text-slate-500 mt-1">{lang.desc}</span>
              </button>
            ))}
          </div>
        </div>

        {/* 2. Topic Selector */}
        <div className="space-y-3">
          <label className="text-xs font-bold uppercase tracking-wider text-slate-400">Topic Area</label>
          <div className="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
            {[
              { id: 'random', name: 'All Topics' },
              { id: 'arrays', name: 'Arrays' },
              { id: 'strings', name: 'Strings' },
              { id: 'hashmap', name: 'HashMap' },
              { id: 'trees', name: 'Trees' },
              { id: 'recursion', name: 'Recursion' },
              { id: 'dp', name: '1D DP' },
              { id: '2ddp', name: '2D DP' },
              { id: 'graphs', name: 'Graphs' },
              { id: 'advanced-dsa', name: 'Adv DSA' }
            ].map((t) => (
              <button
                key={t.id}
                onClick={() => setTopic(t.id as Topic)}
                className={`py-2.5 px-2 rounded-xl border text-center text-xs font-bold transition-all ${
                  topic === t.id
                    ? 'border-indigo-500 bg-indigo-500/10 text-white'
                    : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:border-slate-700'
                }`}
              >
                {t.name}
              </button>
            ))}
          </div>
        </div>


        {/* 3. Difficulty */}
        <div className="space-y-3">
          <label className="text-xs font-bold uppercase tracking-wider text-slate-400">Difficulty</label>
          <div className="grid grid-cols-3 gap-3">
            {[
              { id: 'easy', name: 'Easy', color: 'text-emerald-400' },
              { id: 'medium', name: 'Medium', color: 'text-amber-400' },
              { id: 'hard', name: 'Hard', color: 'text-rose-400' }
            ].map((diff) => (
              <button
                key={diff.id}
                onClick={() => setDifficulty(diff.id as Difficulty)}
                className={`py-3.5 px-3 rounded-xl border text-center transition-all ${
                  difficulty === diff.id
                    ? 'border-indigo-500 bg-indigo-500/10 text-white font-bold'
                    : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:border-slate-700'
                }`}
              >
                <span className={`text-sm font-semibold ${difficulty === diff.id ? 'text-white' : diff.color}`}>
                  {diff.name}
                </span>
              </button>
            ))}
          </div>
        </div>

        {/* 4. Session Mode */}
        <div className="space-y-3">
          <label className="text-xs font-bold uppercase tracking-wider text-slate-400">Timer Mode</label>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <button
              onClick={() => setMode('practice')}
              className={`flex items-start gap-4 p-5 rounded-xl border text-left transition-all ${
                mode === 'practice'
                  ? 'border-indigo-500 bg-indigo-500/10 text-white shadow-[0_0_15px_rgba(99,102,241,0.05)]'
                  : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:border-slate-700'
              }`}
            >
              <div className="mt-1">
                <span className={`flex size-2 rounded-full ${mode === 'practice' ? 'bg-indigo-400' : 'bg-slate-500'}`}></span>
              </div>
              <div className="space-y-1">
                <h4 className="text-sm font-bold text-white">Practice Mode</h4>
                <p className="text-xs text-slate-400">Untimed practice. Inspect solutions, read full explanations, and access logical hints while debugging.</p>
              </div>
            </button>

            <button
              onClick={() => setMode('exam')}
              className={`flex items-start gap-4 p-5 rounded-xl border text-left transition-all ${
                mode === 'exam'
                  ? 'border-indigo-500 bg-indigo-500/10 text-white shadow-[0_0_15px_rgba(99,102,241,0.05)]'
                  : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:border-slate-700'
              }`}
            >
              <div className="mt-1">
                <span className={`flex size-2 rounded-full ${mode === 'exam' ? 'bg-rose-500' : 'bg-slate-500'}`}></span>
              </div>
              <div className="space-y-1">
                <h4 className="text-sm font-bold text-white">Exam Simulation</h4>
                <p className="text-xs text-slate-400">Strict 20-minute timer. No hints or explanations are available. Submission locks code immediately.</p>
              </div>
            </button>
          </div>
        </div>

        <div className="border-t border-slate-800 pt-6">
          <button
            onClick={handleStart}
            disabled={loading}
            className="w-full flex items-center justify-center gap-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm py-4 transition-all hover:shadow-[0_0_20px_rgba(99,102,241,0.4)] disabled:opacity-50"
          >
            {loading ? 'Initializing environment...' : 'Begin Session'}
            {!loading && <ChevronRight className="size-4" />}
          </button>
        </div>
      </div>
    </div>
  );
}
