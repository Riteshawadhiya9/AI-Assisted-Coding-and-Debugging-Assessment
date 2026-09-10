import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Play, BookOpen, CheckCircle, ShieldAlert, ChevronRight } from 'lucide-react';
import type { Attempt } from '../types';

export default function Dashboard() {
  const navigate = useNavigate();
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [stats, setStats] = useState({
    totalAttempted: 12,
    solved: 8,
    accuracy: 67,
    avgTime: '11m 42s',
  });

  useEffect(() => {
    // Load attempts from localStorage or populate mock if empty
    const localData = localStorage.getItem('debuglab_attempts');
    if (localData) {
      const parsed: Attempt[] = JSON.parse(localData);
      setAttempts(parsed);
      
      const solved = parsed.filter(a => a.status === 'passed').length;
      const total = parsed.length;
      const acc = total > 0 ? Math.round((solved / total) * 100) : 0;
      
      let totalTime = 0;
      parsed.forEach(a => totalTime += a.timeSpentSeconds);
      const avgSeconds = total > 0 ? Math.round(totalTime / total) : 0;
      const mins = Math.floor(avgSeconds / 60);
      const secs = avgSeconds % 60;
      
      setStats({
        totalAttempted: total,
        solved,
        accuracy: acc,
        avgTime: total > 0 ? `${mins}m ${secs}s` : '0m 0s',
      });
    } else {
      // Setup mock initial attempts for preview with valid seed IDs
      const mockAttempts: Attempt[] = [
        {
          id: 'att_1',
          questionId: 'q_graph_directed_cycle_dfs',
          questionTitle: 'Directed Graph Cycle Detection',
          language: 'cpp',
          difficulty: 'medium',
          topic: 'graphs',
          mode: 'practice',
          score: 85,
          timeSpentSeconds: 520,
          status: 'passed',
          date: new Date(Date.now() - 24 * 60 * 60 * 1000).toLocaleDateString(),
          codeSubmitted: '',
          bugsDiagnosed: ['incorrect traversal'],
          diagnosedBugType: 'incorrect traversal',
          diagnosisNotes: 'Backtracking recursion state not reset',
          diagnosisCorrect: true,
          testsPassed: 4,
          totalTests: 4,
        },
        {
          id: 'att_2',
          questionId: 'q_tree_validate_bst',
          questionTitle: 'Validate Binary Search Tree',
          language: 'java',
          difficulty: 'medium',
          topic: 'trees',
          mode: 'exam',
          score: 100,
          timeSpentSeconds: 340,
          status: 'passed',
          date: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toLocaleDateString(),
          codeSubmitted: '',
          bugsDiagnosed: ['logical'],
          diagnosedBugType: 'logical',
          diagnosisNotes: 'Only checked immediate children instead of entire subtree bounds',
          diagnosisCorrect: true,
          testsPassed: 4,
          totalTests: 4,
        },
        {
          id: 'att_3',
          questionId: 'q_dp_min_path_sum',
          questionTitle: 'Minimum Path Sum in Grid',
          language: 'c',
          difficulty: 'medium',
          topic: '2ddp',
          mode: 'exam',
          score: 25,
          timeSpentSeconds: 1200,
          status: 'failed',
          date: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000).toLocaleDateString(),
          codeSubmitted: '',
          bugsDiagnosed: [],
          testsPassed: 1,
          totalTests: 4,
        }
      ];
      localStorage.setItem('debuglab_attempts', JSON.stringify(mockAttempts));
      setAttempts(mockAttempts);
    }
  }, []);

  return (
    <div className="w-full max-w-[1700px] px-4 sm:px-6 lg:px-8 py-8 space-y-10 mx-auto">
      {/* Hero Headline */}
      <div className="space-y-4 max-w-3xl">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-indigo-500/25 bg-indigo-500/10 text-xs font-semibold text-indigo-400">
          <span className="h-1.5 w-1.5 rounded-full bg-indigo-400 animate-pulse"></span>
          Practice & Master Stage 3 Coding Debugging
        </div>
        <h1 className="text-4xl md:text-5xl font-black tracking-tight text-white leading-tight">
          Find. Analyze. <span className="text-indigo-500">Fix.</span>
          <br />Validate buggy code in real-time.
        </h1>
        <p className="text-slate-400 text-sm md:text-base max-w-xl leading-relaxed">
          Simulate timed, high-stakes assessments featuring binary trees, dynamic programming, cyclic graphs, and other advanced data structures.
        </p>
      </div>

      {/* Main Mode Selection Row */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Exam Card (Highlight) */}
        <div className="lg:col-span-7 bg-[#111827]/75 border border-indigo-500/30 rounded-2xl p-8 relative overflow-hidden group shadow-[0_0_30px_rgba(99,102,241,0.15)] flex flex-col justify-between min-h-[300px]">
          <div className="absolute top-0 right-0 w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl pointer-events-none group-hover:bg-indigo-600/15 transition-all"></div>
          
          <div className="space-y-4 relative z-10">
            <span className="inline-block px-2.5 py-1 text-[10px] font-bold tracking-wider text-indigo-400 uppercase bg-indigo-950/60 border border-indigo-800/40 rounded-full">
              Assessment Simulation
            </span>
            <h2 className="text-2xl font-bold text-white tracking-tight">Start Debugging Exam</h2>
            <p className="text-slate-400 text-sm max-w-md leading-relaxed">
              1 random advanced DSA debugging question, 20 minutes strict time limit. Compiles and executes code on real test suites. No clues or explanations until submission.
            </p>
          </div>

          <div className="pt-6 relative z-10 flex flex-wrap gap-3">
            <button 
              onClick={() => navigate('/setup?mode=exam')}
              className="inline-flex items-center gap-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm px-6 py-3 transition-all hover:shadow-[0_0_20px_rgba(99,102,241,0.4)] cursor-pointer"
            >
              <Play className="size-4 fill-white" /> Start timed Exam
            </button>
            <button 
              onClick={() => navigate('/problems')}
              className="inline-flex items-center gap-2 rounded-xl border border-slate-700 bg-slate-800/80 hover:bg-slate-700 text-slate-300 font-semibold text-sm px-5 py-3 transition-all cursor-pointer"
            >
              Browse 120 Problems
            </button>
          </div>
        </div>

        {/* Practice Card */}
        <div className="lg:col-span-5 bg-slate-900/50 border border-slate-800 hover:border-slate-700/80 rounded-2xl p-8 flex flex-col justify-between min-h-[300px] transition-all">
          <div className="space-y-4">
            <span className="inline-block px-2.5 py-1 text-[10px] font-bold tracking-wider text-slate-400 uppercase bg-slate-800 border border-slate-700 rounded-full">
              Relaxed Learning
            </span>
            <h2 className="text-2xl font-bold text-white tracking-tight">Practice by Topic</h2>
            <p className="text-slate-400 text-sm leading-relaxed">
              Select your language (C / C++ / Java), pick a specific target topic, select difficulty (Easy/Medium/Hard), and debug at your own pace with optional hints.
            </p>
          </div>

          <div className="pt-6 flex gap-3">
            <button 
              onClick={() => navigate('/setup?mode=practice')}
              className="inline-flex items-center gap-2 rounded-xl border border-slate-700 bg-slate-800 hover:bg-slate-700 text-white font-semibold text-sm px-6 py-3 transition-all cursor-pointer"
            >
              <BookOpen className="size-4 text-slate-400" /> Configure Practice
            </button>
          </div>
        </div>
      </div>

      {/* AI-Assisted Coding Assessment Spotlight Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-purple-950/70 via-indigo-950/60 to-slate-900 border border-purple-500/30 p-7 shadow-[0_0_35px_rgba(168,85,247,0.15)] flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div className="space-y-2 max-w-2xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/15 border border-purple-500/30 text-purple-300 text-xs font-bold">
            <span className="size-1.5 rounded-full bg-purple-400 animate-pulse" />
            <span>NEW MODULE • STAGE 2</span>
          </div>
          <h2 className="text-2xl font-black text-white tracking-tight">
            AI-Assisted Coding Assessment & Practice
          </h2>
          <p className="text-slate-300 text-sm leading-relaxed">
            Pair program with our interactive AI proctor on 50 curated LeetCode-style DSA problems. 
            Evaluate your prompt clarity, context specification, AI collaboration literacy, and algorithmic code correctness in real-time.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3 shrink-0">
          <button
            onClick={() => navigate('/coding/setup')}
            className="inline-flex items-center gap-2 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold text-sm px-6 py-3.5 shadow-lg shadow-purple-600/30 transition-all cursor-pointer active:scale-95"
          >
            <span>Launch AI Coding Lab</span>
            <ChevronRight className="size-4" />
          </button>
        </div>
      </div>


      {/* Analytics Snapshot Row */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-slate-900/40 border border-slate-850 rounded-xl p-5 flex flex-col justify-between">
          <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Attempted</span>
          <div className="flex items-baseline gap-2 mt-2">
            <span className="text-3xl font-black text-white">{stats.totalAttempted}</span>
            <span className="text-xs text-slate-400">questions</span>
          </div>
        </div>
        <div className="bg-slate-900/40 border border-slate-850 rounded-xl p-5 flex flex-col justify-between">
          <span className="text-xs font-semibold text-indigo-400 uppercase tracking-wider">Accuracy</span>
          <div className="flex items-baseline gap-2 mt-2">
            <span className="text-3xl font-black text-indigo-400">{stats.accuracy}%</span>
            <span className="text-xs text-slate-400">pass rate</span>
          </div>
        </div>
        <div className="bg-slate-900/40 border border-slate-850 rounded-xl p-5 flex flex-col justify-between">
          <span className="text-xs font-semibold text-emerald-400 uppercase tracking-wider">Solved</span>
          <div className="flex items-baseline gap-2 mt-2">
            <span className="text-3xl font-black text-emerald-400">{stats.solved}</span>
            <span className="text-xs text-slate-400">successes</span>
          </div>
        </div>
        <div className="bg-slate-900/40 border border-slate-850 rounded-xl p-5 flex flex-col justify-between">
          <span className="text-xs font-semibold text-purple-400 uppercase tracking-wider">Avg Debug Time</span>
          <div className="flex items-baseline gap-2 mt-2">
            <span className="text-3xl font-black text-purple-400">{stats.avgTime}</span>
          </div>
        </div>
      </div>

      {/* Topics & History Division */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 pt-4">
        {/* Left: Quick Topic Selection */}
        <div className="lg:col-span-5 space-y-6">
          <h3 className="text-lg font-bold text-white tracking-tight">Structured Topics</h3>
          <div className="grid grid-cols-1 gap-3">
            {[
              { name: 'Arrays & Two Pointers', count: 'Kadane, Sliding window, Intervals', topic: 'arrays', color: 'border-cyan-500/20 text-cyan-400 bg-cyan-950/20' },
              { name: 'Trees & Binary Search Trees', count: 'BST validation, LCA, Traversals', topic: 'trees', color: 'border-emerald-500/20 text-emerald-400 bg-emerald-950/20' },
              { name: 'Graphs & Cyclic Networks', count: 'DFS, BFS, Dijkstra, Topological', topic: 'graphs', color: 'border-blue-500/20 text-blue-400 bg-blue-950/20' },
              { name: 'Dynamic Programming & Matrix DP', count: '0/1 Knapsack, LCS, 2D Grids', topic: 'dp', color: 'border-purple-500/20 text-purple-400 bg-purple-950/20' },
              { name: 'Advanced DSA Mechanics', count: 'Monotonic stack, Heaps, Lists', topic: 'advanced-dsa', color: 'border-indigo-500/20 text-indigo-400 bg-indigo-950/20' }
            ].map((topic, i) => (
              <div 
                key={i} 
                onClick={() => navigate(`/setup?topic=${topic.topic}`)}
                className="group flex items-center justify-between p-4 rounded-xl border border-slate-800 bg-slate-900/20 hover:bg-slate-800/35 cursor-pointer transition-all"
              >
                <div className="space-y-1">
                  <h4 className="text-sm font-semibold text-white group-hover:text-indigo-400 transition-colors">{topic.name}</h4>
                  <p className="text-xs text-slate-400">{topic.count}</p>
                </div>
                <span className={`px-2 py-0.5 rounded text-[10px] font-bold border ${topic.color}`}>
                  {topic.topic.toUpperCase()}
                </span>
              </div>
            ))}
          </div>
        </div>


        {/* Right: Recent Attempt History */}
        <div className="lg:col-span-7 space-y-6">
          <h3 className="text-lg font-bold text-white tracking-tight">Recent Attempts</h3>
          <div className="space-y-3">
            {attempts.length === 0 ? (
              <div className="text-center py-10 border border-slate-800 rounded-xl bg-slate-900/10 text-slate-400 text-sm">
                No debugging attempts found. Start an exam or practice session!
              </div>
            ) : (
              attempts.slice(0, 5).map((attempt, index) => (
                <div 
                  key={index}
                  className="flex items-center justify-between p-4 border border-slate-800 bg-slate-900/30 rounded-xl hover:border-slate-700 transition-all"
                >
                  <div className="flex items-center gap-3">
                    {attempt.status === 'passed' ? (
                      <CheckCircle className="size-5 text-emerald-500 shrink-0" />
                    ) : (
                      <ShieldAlert className="size-5 text-rose-500 shrink-0" />
                    )}
                    <div className="space-y-1">
                      <h4 className="text-sm font-bold text-white line-clamp-1">{attempt.questionTitle}</h4>
                      <div className="flex flex-wrap items-center gap-x-2 text-[10px] text-slate-400">
                        <span className="uppercase text-slate-300 font-semibold">{attempt.language}</span>
                        <span>•</span>
                        <span className="capitalize">{attempt.topic}</span>
                        <span>•</span>
                        <span>{attempt.date}</span>
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center gap-3 shrink-0">
                    <div className="text-right space-y-0.5">
                      <div className="text-xs font-semibold text-white">Score: {attempt.score}%</div>
                      <div className="text-[10px] text-slate-400">{Math.floor(attempt.timeSpentSeconds / 60)}m {attempt.timeSpentSeconds % 60}s</div>
                    </div>
                    <ChevronRight className="size-4 text-slate-500" />
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
