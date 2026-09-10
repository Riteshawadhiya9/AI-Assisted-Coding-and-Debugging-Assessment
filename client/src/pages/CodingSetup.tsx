import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  Sparkles, ShieldAlert, BookOpen, 
  Search, SlidersHorizontal, ArrowRight, Zap
} from 'lucide-react';
import type { CodingQuestion, CodingLanguage } from '../types';

export default function CodingSetup() {
  const navigate = useNavigate();

  const [questions, setQuestions] = useState<CodingQuestion[]>([]);
  const [loading, setLoading] = useState(true);
  const [mode, setMode] = useState<'practice' | 'assessment'>('practice');
  const [selectedLanguage, setSelectedLanguage] = useState<CodingLanguage>('python');
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('all');
  const [selectedTopic, setSelectedTopic] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    async function fetchQuestions() {
      setLoading(true);
      try {
        const res = await fetch('/api/coding/questions');
        if (res.ok) {
          const data = await res.json();
          setQuestions(data);
        }
      } catch (err) {
        console.error('Failed to load coding questions', err);
      } finally {
        setLoading(false);
      }
    }
    fetchQuestions();
  }, []);

  const topics = Array.from(new Set(questions.map(q => q.topic))).sort();

  const filteredQuestions = questions.filter(q => {
    if (selectedDifficulty !== 'all' && q.difficulty.toLowerCase() !== selectedDifficulty.toLowerCase()) return false;
    if (selectedTopic !== 'all' && q.topic !== selectedTopic) return false;
    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase();
      const desc = (q.description || q.problemStatement || '').toLowerCase();
      return (
        q.title.toLowerCase().includes(query) ||
        desc.includes(query) ||
        q.topic.toLowerCase().includes(query)
      );
    }
    return true;
  });

  const startSession = (questionId: string) => {
    navigate(`/coding/workspace?id=${questionId}&lang=${selectedLanguage}&mode=${mode}`);
  };

  const startRandomSession = () => {
    const list = filteredQuestions.length > 0 ? filteredQuestions : questions;
    if (list.length === 0) return;
    const randomQ = list[Math.floor(Math.random() * list.length)];
    startSession(randomQ.id);
  };

  return (
    <div className="flex-1 py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
      {/* Hero Header */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-950/70 via-slate-900 to-purple-950/60 border border-indigo-500/20 p-8 mb-8 shadow-xl">
        <div className="relative z-10 max-w-3xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-semibold mb-4">
            <Sparkles className="size-3.5" />
            <span>AI-ASSISTED CODING ASSESSMENT</span>
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight mb-3">
            Pair Program with AI to Solve Hard Problems
          </h1>
          <p className="text-slate-300 text-sm leading-relaxed mb-6">
            Practice algorithmic problem solving with real-time AI assistance, or take a proctored AI assessment 
            that evaluates your prompt engineering skills, AI collaboration efficiency, and code correctness.
          </p>

          <div className="flex flex-wrap items-center gap-4">
            <button
              onClick={startRandomSession}
              className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition-all shadow-lg shadow-indigo-600/25 active:scale-95"
            >
              <Zap className="size-4 text-amber-300" />
              <span>Start Quick Challenge</span>
            </button>
            <div className="text-xs text-slate-400 flex items-center gap-2">
              <span className="size-2 rounded-full bg-emerald-400 animate-pulse" />
              <span>{questions.length} DSA Problems Ready</span>
            </div>
          </div>
        </div>
      </div>

      {/* Configuration Controls Bar */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        {/* Mode Selector */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
          <div>
            <label className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2 block">
              Assessment Mode
            </label>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => setMode('practice')}
                className={`flex items-center justify-center gap-2 py-2 px-3 rounded-lg text-xs font-semibold transition-all ${
                  mode === 'practice'
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'bg-slate-800/80 text-slate-300 hover:bg-slate-800'
                }`}
              >
                <BookOpen className="size-3.5" />
                <span>Practice</span>
              </button>
              <button
                type="button"
                onClick={() => setMode('assessment')}
                className={`flex items-center justify-center gap-2 py-2 px-3 rounded-lg text-xs font-semibold transition-all ${
                  mode === 'assessment'
                    ? 'bg-purple-600 text-white shadow-md'
                    : 'bg-slate-800/80 text-slate-300 hover:bg-slate-800'
                }`}
              >
                <ShieldAlert className="size-3.5" />
                <span>Assessment</span>
              </button>
            </div>
          </div>
          <p className="text-[11px] text-slate-400 mt-2">
            {mode === 'practice' 
              ? 'Open interactive mentor with prompt feedback & unlimited hints.' 
              : 'Timed assessment evaluating prompt quality and solution correctness.'}
          </p>
        </div>

        {/* Primary Language */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
          <div>
            <label className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2 block">
              Language Preference
            </label>
            <select
              value={selectedLanguage}
              onChange={(e) => setSelectedLanguage(e.target.value as CodingLanguage)}
              className="w-full bg-slate-800 border border-slate-700 text-slate-200 text-xs rounded-lg px-3 py-2 focus:outline-none focus:border-indigo-500 font-medium"
            >
              <option value="python">Python 3 (Recommended)</option>
              <option value="javascript">JavaScript (Node.js)</option>
              <option value="typescript">TypeScript</option>
              <option value="java">Java 17</option>
              <option value="cpp">C++ (GCC)</option>
            </select>
          </div>
          <p className="text-[11px] text-slate-400 mt-2">
            Starter templates and test harness adapt automatically.
          </p>
        </div>

        {/* Filters Summary */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
          <div>
            <label className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2 block">
              Filters & Search
            </label>
            <div className="relative">
              <Search className="size-3.5 text-slate-400 absolute left-3 top-2.5" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search problems by keyword..."
                className="w-full bg-slate-800 border border-slate-700 text-slate-200 text-xs rounded-lg pl-8 pr-3 py-2 focus:outline-none focus:border-indigo-500"
              />
            </div>
          </div>
          <div className="flex items-center justify-between text-[11px] text-slate-400 mt-2">
            <span>Showing {filteredQuestions.length} of {questions.length} problems</span>
          </div>
        </div>
      </div>

      {/* Filter Tags */}
      <div className="flex flex-wrap items-center gap-2 mb-6">
        <div className="flex items-center gap-1 text-xs text-slate-400 mr-2">
          <SlidersHorizontal className="size-3.5" />
          <span>Difficulty:</span>
        </div>
        {['all', 'easy', 'medium', 'hard'].map((diff) => (
          <button
            key={diff}
            onClick={() => setSelectedDifficulty(diff)}
            className={`px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider transition-colors ${
              selectedDifficulty === diff
                ? 'bg-indigo-600 text-white'
                : 'bg-slate-900 border border-slate-800 text-slate-400 hover:text-white'
            }`}
          >
            {diff}
          </button>
        ))}

        <div className="h-4 w-px bg-slate-800 mx-2" />

        <div className="flex items-center gap-1 text-xs text-slate-400 mr-2">
          <span>Topic:</span>
        </div>
        <select
          value={selectedTopic}
          onChange={(e) => setSelectedTopic(e.target.value)}
          className="bg-slate-900 border border-slate-800 text-slate-300 text-xs rounded-lg px-2.5 py-1 focus:outline-none focus:border-indigo-500"
        >
          <option value="all">All Topics</option>
          {topics.map(t => (
            <option key={t} value={t}>{t}</option>
          ))}
        </select>
      </div>

      {/* Questions Table / List */}
      <div className="bg-slate-900/60 border border-slate-800 rounded-xl overflow-hidden">
        <div className="grid grid-cols-12 px-6 py-3 bg-slate-900 border-b border-slate-800 text-[11px] font-bold uppercase tracking-wider text-slate-400">
          <div className="col-span-1">#</div>
          <div className="col-span-5">Title</div>
          <div className="col-span-2">Difficulty</div>
          <div className="col-span-2">Topic</div>
          <div className="col-span-2 text-right">Action</div>
        </div>

        {loading ? (
          <div className="py-12 text-center text-slate-400 text-xs">
            Loading problem bank...
          </div>
        ) : filteredQuestions.length === 0 ? (
          <div className="py-12 text-center text-slate-400 text-xs">
            No questions matched your search criteria.
          </div>
        ) : (
          <div className="divide-y divide-slate-800/60">
            {filteredQuestions.map((q, idx) => {
              const diffNormalized = q.difficulty ? q.difficulty.toLowerCase() : 'medium';
              const diffLabel = diffNormalized.charAt(0).toUpperCase() + diffNormalized.slice(1);
              return (
                <div
                  key={q.id}
                  onClick={() => startSession(q.id)}
                  className="grid grid-cols-12 px-6 py-3.5 items-center hover:bg-slate-800/40 cursor-pointer transition-colors group text-xs"
                >
                  <div className="col-span-1 text-slate-500 font-mono font-semibold">
                    {q.number ?? (idx + 1)}
                  </div>
                  <div className="col-span-5 font-semibold text-slate-200 group-hover:text-indigo-300 transition-colors">
                    {q.title}
                  </div>
                  <div className="col-span-2">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${
                      diffNormalized === 'easy' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' :
                      diffNormalized === 'medium' ? 'bg-amber-500/10 text-amber-400 border-amber-500/20' :
                      'bg-rose-500/10 text-rose-400 border-rose-500/20'
                    }`}>
                      {diffLabel}
                    </span>
                  </div>
                  <div className="col-span-2 text-slate-400">
                    <span className="bg-slate-800/60 px-2 py-0.5 rounded text-[11px] border border-slate-700/40">
                      {q.topic}
                    </span>
                  </div>
                  <div className="col-span-2 text-right">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        startSession(q.id);
                      }}
                      className="inline-flex items-center gap-1.5 px-3 py-1 bg-indigo-600/80 hover:bg-indigo-600 text-white rounded-lg text-xs font-semibold transition-colors"
                    >
                      <span>Code</span>
                      <ArrowRight className="size-3" />
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
