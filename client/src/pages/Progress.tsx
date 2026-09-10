import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  BarChart2, CheckCircle2, Award, Clock, Trash2, 
  XCircle, AlertTriangle, Code, Target, Bug, ArrowRight 
} from 'lucide-react';
import type { Attempt, Language, Difficulty } from '../types';

export default function Progress() {
  const navigate = useNavigate();
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [stats, setStats] = useState({
    total: 0,
    solved: 0,
    failed: 0,
    accuracy: 0,
    avgScore: 0,
    avgTimeSeconds: 0,
    topicStats: {} as Record<string, { solved: number; total: number }>,
    languageStats: {
      c: { solved: 0, total: 0 },
      cpp: { solved: 0, total: 0 },
      java: { solved: 0, total: 0 }
    },
    difficultyStats: {
      easy: { solved: 0, total: 0 },
      medium: { solved: 0, total: 0 },
      hard: { solved: 0, total: 0 }
    },
    bugTypeCounts: {} as Record<string, number>,
    weakTopics: [] as { topic: string; accuracy: number; total: number }[]
  });

  const loadProgress = () => {
    const data = localStorage.getItem('debuglab_attempts');
    if (data) {
      const parsed: Attempt[] = JSON.parse(data);
      setAttempts(parsed);

      const total = parsed.length;
      const solved = parsed.filter(a => a.status === 'passed').length;
      const failed = total - solved;
      const accuracy = total > 0 ? Math.round((solved / total) * 100) : 0;
      
      const totalScore = parsed.reduce((sum, a) => sum + (a.score || 0), 0);
      const avgScore = total > 0 ? Math.round(totalScore / total) : 0;

      const totalTime = parsed.reduce((sum, a) => sum + (a.timeSpentSeconds || 0), 0);
      const avgTimeSeconds = total > 0 ? Math.round(totalTime / total) : 0;

      // Topic stats
      const topicStats: Record<string, { solved: number; total: number }> = {};
      // Language stats
      const languageStats: Record<Language, { solved: number; total: number }> = {
        c: { solved: 0, total: 0 },
        cpp: { solved: 0, total: 0 },
        java: { solved: 0, total: 0 }
      };
      // Difficulty stats
      const difficultyStats: Record<Difficulty, { solved: number; total: number }> = {
        easy: { solved: 0, total: 0 },
        medium: { solved: 0, total: 0 },
        hard: { solved: 0, total: 0 }
      };
      // Common bug types
      const bugTypeCounts: Record<string, number> = {};

      parsed.forEach(a => {
        // Topic
        if (a.topic) {
          if (!topicStats[a.topic]) {
            topicStats[a.topic] = { solved: 0, total: 0 };
          }
          topicStats[a.topic].total += 1;
          if (a.status === 'passed') {
            topicStats[a.topic].solved += 1;
          }
        }

        // Language
        if (a.language && languageStats[a.language]) {
          languageStats[a.language].total += 1;
          if (a.status === 'passed') {
            languageStats[a.language].solved += 1;
          }
        }

        // Difficulty
        if (a.difficulty && difficultyStats[a.difficulty]) {
          difficultyStats[a.difficulty].total += 1;
          if (a.status === 'passed') {
            difficultyStats[a.difficulty].solved += 1;
          }
        }

        // Bug types
        const bugType = a.diagnosedBugType || (a.bugsDiagnosed && a.bugsDiagnosed[0]);
        if (bugType) {
          bugTypeCounts[bugType] = (bugTypeCounts[bugType] || 0) + 1;
        }
      });

      // Compute weak topics (< 60% accuracy with at least 1 attempt)
      const weakTopics = Object.entries(topicStats)
        .map(([topic, stat]) => ({
          topic,
          accuracy: Math.round((stat.solved / stat.total) * 100),
          total: stat.total
        }))
        .filter(t => t.accuracy < 60)
        .sort((a, b) => a.accuracy - b.accuracy);

      setStats({
        total,
        solved,
        failed,
        accuracy,
        avgScore,
        avgTimeSeconds,
        topicStats,
        languageStats,
        difficultyStats,
        bugTypeCounts,
        weakTopics
      });
    }
  };

  useEffect(() => {
    loadProgress();
  }, []);

  const handleClearHistory = () => {
    if (window.confirm('Are you sure you want to clear your attempt history? This will delete all saved stats permanently.')) {
      localStorage.removeItem('debuglab_attempts');
      setAttempts([]);
      setStats({
        total: 0,
        solved: 0,
        failed: 0,
        accuracy: 0,
        avgScore: 0,
        avgTimeSeconds: 0,
        topicStats: {},
        languageStats: {
          c: { solved: 0, total: 0 },
          cpp: { solved: 0, total: 0 },
          java: { solved: 0, total: 0 }
        },
        difficultyStats: {
          easy: { solved: 0, total: 0 },
          medium: { solved: 0, total: 0 },
          hard: { solved: 0, total: 0 }
        },
        bugTypeCounts: {},
        weakTopics: []
      });
    }
  };

  const formatDuration = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}m ${secs}s`;
  };

  return (
    <div className="mx-auto max-w-[1240px] px-6 md:px-10 py-10 relative z-10 space-y-8">
      {/* Title */}
      <div className="flex items-center justify-between flex-wrap gap-4 border-b border-slate-800 pb-6">
        <div className="space-y-1">
          <h1 className="text-3xl font-black tracking-tight text-white flex items-center gap-2">
            <BarChart2 className="size-8 text-indigo-500" /> Performance & Analytics
          </h1>
          <p className="text-slate-400 text-sm">
            Comprehensive diagnostic debugging analytics across topics, languages, difficulties, and common bug patterns.
          </p>
        </div>
        {attempts.length > 0 && (
          <button
            onClick={handleClearHistory}
            className="flex items-center gap-1.5 rounded-lg border border-rose-500/30 hover:border-rose-500 bg-rose-950/20 text-rose-400 font-semibold text-xs py-2.5 px-4 transition-all cursor-pointer"
          >
            <Trash2 className="size-3.5" /> Clear History
          </button>
        )}
      </div>

      {/* Main stat cards: Total, Solved vs Failed, Avg Time, Avg Score */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {[
          { 
            label: 'Total Assessments', 
            value: stats.total, 
            sub: `${stats.accuracy}% overall accuracy`,
            icon: Award, 
            color: 'text-indigo-400' 
          },
          { 
            label: 'Solved vs Failed', 
            value: `${stats.solved} / ${stats.failed}`, 
            sub: `${stats.solved} solved • ${stats.failed} failed`,
            icon: CheckCircle2, 
            color: 'text-emerald-400' 
          },
          { 
            label: 'Avg Debugging Time', 
            value: formatDuration(stats.avgTimeSeconds), 
            sub: 'Per completed question',
            icon: Clock, 
            color: 'text-amber-400' 
          },
          { 
            label: 'Average Score', 
            value: `${stats.avgScore}%`, 
            sub: 'Includes tests & diagnosis',
            icon: BarChart2, 
            color: 'text-purple-400' 
          }
        ].map((item, i) => (
          <div key={i} className="bg-slate-900/40 border border-slate-800 rounded-xl p-5 flex items-center gap-4">
            <div className={`p-3 rounded-lg bg-slate-950/50 border border-slate-800/80 ${item.color}`}>
              <item.icon className="size-6" />
            </div>
            <div>
              <span className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">{item.label}</span>
              <div className="text-2xl font-black text-white mt-0.5">{item.value}</div>
              <span className="text-[11px] text-slate-400">{item.sub}</span>
            </div>
          </div>
        ))}
      </div>

      {/* Weak Topics Section */}
      {stats.weakTopics.length > 0 && (
        <div className="bg-amber-950/20 border border-amber-500/30 rounded-2xl p-5 space-y-3">
          <div className="flex items-center gap-2 text-amber-400 font-bold text-sm">
            <AlertTriangle className="size-4" />
            <span>Targeted Weak Topic Detection</span>
          </div>
          <p className="text-slate-300 text-xs leading-relaxed">
            The following topics have an accuracy below 60%. Prioritize practicing them to improve your assessment score:
          </p>
          <div className="flex flex-wrap gap-2.5 pt-1">
            {stats.weakTopics.map(wt => (
              <button
                key={wt.topic}
                onClick={() => navigate(`/practice?topic=${wt.topic}`)}
                className="flex items-center gap-2 px-3 py-1.5 bg-amber-900/30 hover:bg-amber-800/40 border border-amber-500/40 rounded-lg text-xs font-semibold text-amber-200 transition-all cursor-pointer"
              >
                <span className="capitalize">{wt.topic}</span>
                <span className="text-rose-400 font-bold">({wt.accuracy}% passed)</span>
                <ArrowRight className="size-3 text-amber-400" />
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Accuracy Breakdowns: Topic, Language, Difficulty */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* 1. Topic Accuracy */}
        <div className="bg-[#111827]/30 border border-slate-800 rounded-2xl p-6 space-y-5">
          <h3 className="text-sm font-bold text-white tracking-tight flex items-center gap-2">
            <Target className="size-4 text-indigo-400" /> Topic Accuracy
          </h3>
          <div className="space-y-3.5">
            {Object.keys(stats.topicStats).length === 0 ? (
              <p className="text-xs text-slate-500 py-4 text-center">No topic data yet.</p>
            ) : (
              Object.entries(stats.topicStats).map(([topic, stat]) => {
                const pct = stat.total > 0 ? Math.round((stat.solved / stat.total) * 100) : 0;
                return (
                  <div key={topic} className="space-y-1.5">
                    <div className="flex items-center justify-between text-xs font-semibold">
                      <span className="text-slate-300 capitalize">{topic}</span>
                      <span className="text-slate-400 font-mono">
                        {stat.solved}/{stat.total} ({pct}%)
                      </span>
                    </div>
                    <div className="w-full h-2 bg-slate-950 border border-slate-800 rounded-full overflow-hidden">
                      <div 
                        className={`h-full rounded-full transition-all duration-500 ${
                          pct >= 75 ? 'bg-emerald-500' : pct >= 50 ? 'bg-amber-500' : 'bg-rose-500'
                        }`}
                        style={{ width: `${pct}%` }}
                      ></div>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>

        {/* 2. Language Accuracy */}
        <div className="bg-[#111827]/30 border border-slate-800 rounded-2xl p-6 space-y-5">
          <h3 className="text-sm font-bold text-white tracking-tight flex items-center gap-2">
            <Code className="size-4 text-emerald-400" /> Language Accuracy
          </h3>
          <div className="space-y-3.5">
            {[
              { id: 'c', label: 'C Language', stat: stats.languageStats.c },
              { id: 'cpp', label: 'C++', stat: stats.languageStats.cpp },
              { id: 'java', label: 'Java', stat: stats.languageStats.java }
            ].map(lang => {
              const pct = lang.stat.total > 0 ? Math.round((lang.stat.solved / lang.stat.total) * 100) : 0;
              return (
                <div key={lang.id} className="space-y-1.5">
                  <div className="flex items-center justify-between text-xs font-semibold">
                    <span className="text-slate-300">{lang.label}</span>
                    <span className="text-slate-400 font-mono">
                      {lang.stat.solved}/{lang.stat.total} ({pct}%)
                    </span>
                  </div>
                  <div className="w-full h-2 bg-slate-950 border border-slate-800 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-emerald-500 rounded-full transition-all duration-500"
                      style={{ width: `${pct}%` }}
                    ></div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* 3. Difficulty Accuracy */}
        <div className="bg-[#111827]/30 border border-slate-800 rounded-2xl p-6 space-y-5">
          <h3 className="text-sm font-bold text-white tracking-tight flex items-center gap-2">
            <Award className="size-4 text-amber-400" /> Difficulty Accuracy
          </h3>
          <div className="space-y-3.5">
            {[
              { id: 'easy', label: 'Easy', stat: stats.difficultyStats.easy, color: 'bg-emerald-500' },
              { id: 'medium', label: 'Medium', stat: stats.difficultyStats.medium, color: 'bg-amber-500' },
              { id: 'hard', label: 'Hard', stat: stats.difficultyStats.hard, color: 'bg-rose-500' }
            ].map(diff => {
              const pct = diff.stat.total > 0 ? Math.round((diff.stat.solved / diff.stat.total) * 100) : 0;
              return (
                <div key={diff.id} className="space-y-1.5">
                  <div className="flex items-center justify-between text-xs font-semibold">
                    <span className="text-slate-300">{diff.label}</span>
                    <span className="text-slate-400 font-mono">
                      {diff.stat.solved}/{diff.stat.total} ({pct}%)
                    </span>
                  </div>
                  <div className="w-full h-2 bg-slate-950 border border-slate-800 rounded-full overflow-hidden">
                    <div 
                      className={`h-full ${diff.color} rounded-full transition-all duration-500`}
                      style={{ width: `${pct}%` }}
                    ></div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Common Bug Types Section */}
      <div className="bg-[#111827]/30 border border-slate-800 rounded-2xl p-6 space-y-4">
        <h3 className="text-sm font-bold text-white tracking-tight flex items-center gap-2">
          <Bug className="size-4 text-purple-400" /> Common Bug Types Encountered
        </h3>
        <p className="text-slate-400 text-xs">
          Frequency of bug categories you have identified or encountered across debugging sessions:
        </p>
        <div className="flex flex-wrap gap-2.5 pt-1">
          {Object.keys(stats.bugTypeCounts).length === 0 ? (
            <p className="text-xs text-slate-500 py-2">No bug type diagnoses recorded yet.</p>
          ) : (
            Object.entries(stats.bugTypeCounts)
              .sort((a, b) => b[1] - a[1])
              .map(([bugType, count]) => (
                <div 
                  key={bugType}
                  className="px-3 py-1.5 bg-slate-900 border border-slate-800 rounded-lg flex items-center gap-2 text-xs"
                >
                  <span className="text-slate-300 capitalize">{bugType}</span>
                  <span className="px-1.5 py-0.5 rounded bg-indigo-950/60 border border-indigo-900/40 text-indigo-400 font-bold text-[10px]">
                    {count} {count === 1 ? 'time' : 'times'}
                  </span>
                </div>
              ))
          )}
        </div>
      </div>

      {/* Historical List table */}
      <div className="bg-[#111827]/10 border border-slate-800 rounded-2xl p-6 space-y-6">
        <h3 className="text-sm font-bold text-white tracking-tight">Attempt History</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-slate-800 text-slate-500 uppercase tracking-wider font-bold">
                <th className="py-3 px-4">Status</th>
                <th className="py-3 px-4">Question</th>
                <th className="py-3 px-4">Language</th>
                <th className="py-3 px-4">Topic</th>
                <th className="py-3 px-4">Difficulty</th>
                <th className="py-3 px-4 text-center">Score</th>
                <th className="py-3 px-4 text-center">Time</th>
                <th className="py-3 px-4 text-right">Date</th>
              </tr>
            </thead>
            <tbody>
              {attempts.length === 0 ? (
                <tr>
                  <td colSpan={8} className="py-8 text-center text-slate-500 font-medium">
                    No debugging attempts tracked yet. Run a practice workspace to seed results!
                  </td>
                </tr>
              ) : (
                attempts.map((att, i) => (
                  <tr 
                    key={i} 
                    onClick={() => navigate(`/results?attemptId=${att.id}`)}
                    className="border-b border-slate-800/50 hover:bg-slate-900/20 cursor-pointer transition-all"
                  >
                    <td className="py-3.5 px-4">
                      {att.status === 'passed' ? (
                        <span className="inline-flex items-center gap-1 text-emerald-400 font-semibold bg-emerald-950/20 border border-emerald-900/30 px-2 py-0.5 rounded">
                          <CheckCircle2 className="size-3" /> PASSED
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 text-rose-400 font-semibold bg-rose-950/20 border border-rose-900/30 px-2 py-0.5 rounded">
                          <XCircle className="size-3" /> FAILED
                        </span>
                      )}
                    </td>
                    <td className="py-3.5 px-4 font-bold text-white">{att.questionTitle}</td>
                    <td className="py-3.5 px-4 font-mono uppercase text-slate-400">{att.language}</td>
                    <td className="py-3.5 px-4 capitalize text-slate-400">{att.topic}</td>
                    <td className="py-3.5 px-4 capitalize text-slate-400">{att.difficulty}</td>
                    <td className="py-3.5 px-4 text-center font-bold text-white">{att.score}%</td>
                    <td className="py-3.5 px-4 text-center font-mono text-slate-400">
                      {att.timeSpentSeconds ? formatDuration(att.timeSpentSeconds) : '—'}
                    </td>
                    <td className="py-3.5 px-4 text-right text-slate-500">{att.date}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
