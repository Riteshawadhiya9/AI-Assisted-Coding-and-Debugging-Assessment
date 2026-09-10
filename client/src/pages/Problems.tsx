import { useEffect, useState, useMemo } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
  Search, CheckCircle2, Circle, Code2, 
  ArrowUpDown, Play, Sparkles
} from 'lucide-react';
import type { Question, Attempt } from '../types';

export default function Problems() {
  const navigate = useNavigate();
  const [questions, setQuestions] = useState<Question[]>([]);
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Filter states
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedLanguage, setSelectedLanguage] = useState<string>('all');
  const [selectedTopic, setSelectedTopic] = useState<string>('all');
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('all');
  const [selectedStatus, setSelectedStatus] = useState<'all' | 'solved' | 'unsolved'>('all');
  const [sortBy, setSortBy] = useState<'id' | 'title' | 'difficulty'>('id');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');

  useEffect(() => {
    async function fetchQuestions() {
      try {
        const res = await fetch('/api/questions');
        if (!res.ok) throw new Error('Failed to fetch question bank');
        const data = await res.json();
        setQuestions(data);

        // Load attempts for solved status
        const local = localStorage.getItem('debuglab_attempts');
        if (local) {
          setAttempts(JSON.parse(local));
        }
      } catch (err: any) {
        setError(err.message || 'Error loading problems.');
      } finally {
        setLoading(false);
      }
    }
    fetchQuestions();
  }, []);

  // Map of solved question IDs
  const solvedQuestionIds = useMemo(() => {
    const solvedSet = new Set<string>();
    attempts.forEach(a => {
      if (a.status === 'passed') {
        solvedSet.add(a.questionId);
      }
    });
    return solvedSet;
  }, [attempts]);

  // Filtered and sorted questions
  const filteredQuestions = useMemo(() => {
    return questions.filter((q) => {
      // 1. Search Query
      if (searchQuery.trim()) {
        const qLower = searchQuery.toLowerCase();
        const matchesTitle = q.title.toLowerCase().includes(qLower);
        const matchesSubtopic = q.subtopic.toLowerCase().includes(qLower);
        const matchesTags = q.tags?.some(t => t.toLowerCase().includes(qLower));
        if (!matchesTitle && !matchesSubtopic && !matchesTags) return false;
      }

      // 2. Language Filter
      if (selectedLanguage !== 'all') {
        const hasLang = q.implementations?.[selectedLanguage as keyof typeof q.implementations] !== undefined;
        const matchesLegacy = q.language?.toLowerCase() === selectedLanguage.toLowerCase();
        if (!hasLang && !matchesLegacy) return false;
      }

      // 3. Topic Filter
      if (selectedTopic !== 'all') {
        if (selectedTopic === 'trees' && q.topic !== 'trees') return false;
        if (selectedTopic === 'graphs' && q.topic !== 'graphs') return false;
        if (selectedTopic === '2ddp' && q.topic !== '2ddp') return false;
        if (selectedTopic === 'advanced-dsa' && q.topic !== 'advanced-dsa') return false;
      }

      // 4. Difficulty Filter
      if (selectedDifficulty !== 'all' && q.difficulty.toLowerCase() !== selectedDifficulty.toLowerCase()) {
        return false;
      }

      // 5. Status Filter
      if (selectedStatus === 'solved' && !solvedQuestionIds.has(q.id)) return false;
      if (selectedStatus === 'unsolved' && solvedQuestionIds.has(q.id)) return false;

      return true;
    }).sort((a, b) => {
      let comparison = 0;
      if (sortBy === 'id') {
        comparison = a.id.localeCompare(b.id);
      } else if (sortBy === 'title') {
        comparison = a.title.localeCompare(b.title);
      } else if (sortBy === 'difficulty') {
        const diffWeight: Record<string, number> = { easy: 1, medium: 2, hard: 3 };
        comparison = (diffWeight[a.difficulty] || 0) - (diffWeight[b.difficulty] || 0);
      }
      return sortOrder === 'asc' ? comparison : -comparison;
    });
  }, [questions, searchQuery, selectedLanguage, selectedTopic, selectedDifficulty, selectedStatus, sortBy, sortOrder, solvedQuestionIds]);

  const handleRandomPick = () => {
    if (filteredQuestions.length === 0) return;
    const randIdx = Math.floor(Math.random() * filteredQuestions.length);
    navigate(`/workspace?id=${filteredQuestions[randIdx].id}&mode=practice`);
  };

  if (loading) {
    return (
      <div className="flex h-[80vh] items-center justify-center text-slate-400">
        <div className="text-center space-y-4">
          <span className="relative flex h-8 w-8 mx-auto">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-8 w-8 bg-indigo-500"></span>
          </span>
          <p className="text-sm font-semibold">Loading Problem Bank...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-10 text-center text-rose-400 space-y-4">
        <p className="font-bold text-lg">Error loading problems</p>
        <p className="text-xs text-slate-400">{error}</p>
      </div>
    );
  }

  const totalCount = questions.length;
  const solvedCount = solvedQuestionIds.size;
  const solvedPercent = totalCount > 0 ? Math.round((solvedCount / totalCount) * 100) : 0;

  return (
    <div className="w-full px-4 sm:px-6 lg:px-8 py-8 space-y-6 max-w-[1700px] mx-auto">
      {/* 1. Page Header & Stats Banner */}
      <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 bg-[#0f172a]/60 border border-slate-800 rounded-2xl p-6 backdrop-blur-md">
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <Code2 className="size-6 text-indigo-400" />
            <h1 className="text-2xl font-black text-white tracking-tight">Question Bank</h1>
          </div>
          <p className="text-xs text-slate-400 font-medium">
            Browse, search, and practice {questions.length}+ language-independent algorithmic debugging challenges across Arrays, Strings, HashMaps, Trees, Recursion, DP, Graphs, and Advanced DSA in C, C++, and Java.
          </p>
        </div>

        {/* Solved Progress Overview */}
        <div className="flex items-center gap-4 bg-slate-900/80 border border-slate-800 rounded-xl px-5 py-3 shrink-0">
          <div>
            <div className="text-[10px] uppercase font-bold tracking-wider text-slate-500">Solved Ratio</div>
            <div className="text-xl font-black text-white font-mono mt-0.5">
              <span className="text-emerald-400">{solvedCount}</span> / {totalCount}
              <span className="text-xs text-slate-500 font-normal ml-2">({solvedPercent}%)</span>
            </div>
          </div>
          <div className="h-8 w-px bg-slate-800"></div>
          <button
            onClick={handleRandomPick}
            className="flex items-center gap-1.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs py-2 px-3.5 rounded-lg transition-all shadow-[0_0_12px_rgba(99,102,241,0.3)] cursor-pointer"
          >
            <Sparkles className="size-3.5" /> Pick Random
          </button>
        </div>
      </div>

      {/* 2. Search & Filter Bar */}
      <div className="bg-[#0f172a]/40 border border-slate-800 rounded-2xl p-4 space-y-3 backdrop-blur-md">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-12 gap-3 items-center">
          {/* Search Input (col-span-4) */}
          <div className="lg:col-span-4 relative">
            <Search className="size-4 text-slate-500 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search problems by name or tag..."
              className="w-full bg-[#070b13] border border-slate-800 rounded-xl pl-9 pr-4 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            />
          </div>

          {/* Topic Dropdown (col-span-2) */}
          <div className="lg:col-span-2">
            <select
              value={selectedTopic}
              onChange={(e) => setSelectedTopic(e.target.value)}
              className="w-full bg-[#070b13] border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-300 focus:outline-none focus:border-indigo-500"
            >
              <option value="all">All Topics ({questions.length})</option>
              <option value="arrays">Arrays</option>
              <option value="strings">Strings</option>
              <option value="hashmap">HashMap / Set</option>
              <option value="trees">Trees & BST</option>
              <option value="recursion">Recursion & Backtracking</option>
              <option value="dp">Dynamic Programming</option>
              <option value="2ddp">2D / Matrix DP</option>
              <option value="graphs">Graphs</option>
              <option value="advanced-dsa">Advanced DSA</option>
            </select>
          </div>

          {/* Difficulty Dropdown (col-span-2) */}
          <div className="lg:col-span-2">
            <select
              value={selectedDifficulty}
              onChange={(e) => setSelectedDifficulty(e.target.value)}
              className="w-full bg-[#070b13] border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-300 focus:outline-none focus:border-indigo-500"
            >
              <option value="all">All Difficulties</option>
              <option value="easy">Easy</option>
              <option value="medium">Medium</option>
              <option value="hard">Hard</option>
            </select>
          </div>

          {/* Language Dropdown (col-span-2) */}
          <div className="lg:col-span-2">
            <select
              value={selectedLanguage}
              onChange={(e) => setSelectedLanguage(e.target.value)}
              className="w-full bg-[#070b13] border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-300 focus:outline-none focus:border-indigo-500"
            >
              <option value="all">All Languages (C, C++, Java)</option>
              <option value="c">C</option>
              <option value="cpp">C++</option>
              <option value="java">Java</option>
            </select>
          </div>

          {/* Status Dropdown (col-span-2) */}
          <div className="lg:col-span-2">
            <select
              value={selectedStatus}
              onChange={(e) => setSelectedStatus(e.target.value as any)}
              className="w-full bg-[#070b13] border border-slate-800 rounded-xl px-3 py-2 text-xs text-slate-300 focus:outline-none focus:border-indigo-500"
            >
              <option value="all">All Status</option>
              <option value="solved">Solved Only</option>
              <option value="unsolved">Unsolved Only</option>
            </select>
          </div>
        </div>
      </div>

      {/* 3. Problems Table */}
      <div className="bg-[#0f172a]/30 border border-slate-800 rounded-2xl overflow-hidden shadow-2xl">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-[#0f172a]/90 border-b border-slate-800 text-[11px] font-bold uppercase tracking-wider text-slate-400 select-none">
                <th className="py-3 px-4 w-12 text-center">Status</th>
                <th 
                  onClick={() => {
                    if (sortBy === 'id') setSortOrder(prev => prev === 'asc' ? 'desc' : 'asc');
                    else { setSortBy('id'); setSortOrder('asc'); }
                  }}
                  className="py-3 px-4 w-16 cursor-pointer hover:text-white"
                >
                  <div className="flex items-center gap-1">
                    <span>#</span>
                    <ArrowUpDown className="size-3" />
                  </div>
                </th>
                <th 
                  onClick={() => {
                    if (sortBy === 'title') setSortOrder(prev => prev === 'asc' ? 'desc' : 'asc');
                    else { setSortBy('title'); setSortOrder('asc'); }
                  }}
                  className="py-3 px-4 cursor-pointer hover:text-white"
                >
                  <div className="flex items-center gap-1">
                    <span>Title</span>
                    <ArrowUpDown className="size-3" />
                  </div>
                </th>
                <th className="py-3 px-4 w-32">Topic</th>
                <th className="py-3 px-4 w-36">Supported</th>
                <th 
                  onClick={() => {
                    if (sortBy === 'difficulty') setSortOrder(prev => prev === 'asc' ? 'desc' : 'asc');
                    else { setSortBy('difficulty'); setSortOrder('asc'); }
                  }}
                  className="py-3 px-4 w-28 cursor-pointer hover:text-white"
                >
                  <div className="flex items-center gap-1">
                    <span>Difficulty</span>
                    <ArrowUpDown className="size-3" />
                  </div>
                </th>
                <th className="py-3 px-4 w-28 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 text-xs">
              {filteredQuestions.length === 0 ? (
                <tr>
                  <td colSpan={7} className="py-12 text-center text-slate-500">
                    No questions match the selected search & filter criteria.
                  </td>
                </tr>
              ) : (
                filteredQuestions.map((q, idx) => {
                  const isSolved = solvedQuestionIds.has(q.id);
                  const activeLang = selectedLanguage !== 'all' ? selectedLanguage : 'cpp';
                  return (
                    <tr 
                      key={q.id}
                      className="hover:bg-slate-800/40 transition-colors group cursor-pointer"
                      onClick={() => navigate(`/workspace?id=${q.id}&mode=practice&lang=${activeLang}`)}
                    >
                      {/* Status */}
                      <td className="py-3.5 px-4 text-center">
                        {isSolved ? (
                          <CheckCircle2 className="size-4 text-emerald-400 mx-auto" />
                        ) : (
                          <Circle className="size-3.5 text-slate-600 mx-auto" />
                        )}
                      </td>

                      {/* Number */}
                      <td className="py-3.5 px-4 font-mono text-slate-500 font-semibold">
                        {idx + 1}
                      </td>

                      {/* Title */}
                      <td className="py-3.5 px-4">
                        <div className="flex items-center gap-2">
                          <span className="font-bold text-slate-200 group-hover:text-indigo-400 transition-colors">
                            {q.title}
                          </span>
                          {q.visualData && (
                            <span className="text-[9px] font-bold text-amber-400 bg-amber-950/30 border border-amber-900/40 px-1.5 py-0.2 rounded uppercase">
                              Visual
                            </span>
                          )}
                        </div>
                        <div className="text-[11px] text-slate-500 truncate max-w-md mt-0.5">
                          {q.subtopic} • {q.tags?.slice(0, 3).join(', ')}
                        </div>
                      </td>

                      {/* Topic */}
                      <td className="py-3.5 px-4">
                        <span className="text-[11px] font-semibold text-slate-400 bg-slate-900 border border-slate-800 px-2.5 py-1 rounded-full capitalize">
                          {q.topic}
                        </span>
                      </td>

                      {/* Language badges */}
                      <td className="py-3.5 px-4">
                        <div className="flex items-center gap-1 font-mono text-[10px]">
                          <span className="bg-slate-900 text-indigo-300 border border-slate-800 px-1.5 py-0.5 rounded font-bold">C</span>
                          <span className="bg-slate-900 text-indigo-300 border border-slate-800 px-1.5 py-0.5 rounded font-bold">C++</span>
                          <span className="bg-slate-900 text-indigo-300 border border-slate-800 px-1.5 py-0.5 rounded font-bold">Java</span>
                        </div>
                      </td>

                      {/* Difficulty */}
                      <td className="py-3.5 px-4">
                        <span className={`text-[11px] font-bold capitalize ${
                          q.difficulty === 'easy' ? 'text-emerald-400' :
                          q.difficulty === 'medium' ? 'text-amber-400' : 'text-rose-400'
                        }`}>
                          {q.difficulty}
                        </span>
                      </td>

                      {/* Action */}
                      <td className="py-3.5 px-4 text-right">
                        <Link
                          to={`/workspace?id=${q.id}&mode=practice&lang=${activeLang}`}
                          onClick={(e) => e.stopPropagation()}
                          className="inline-flex items-center gap-1 text-xs font-bold text-indigo-400 hover:text-white bg-indigo-950/30 hover:bg-indigo-600 border border-indigo-900/40 px-3 py-1.5 rounded-lg transition-all"
                        >
                          <Play className="size-3 fill-current" />
                          <span>Debug</span>
                        </Link>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </div>

    </div>
  );
}
