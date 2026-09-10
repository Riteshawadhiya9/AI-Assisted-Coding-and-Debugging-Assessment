import { Link, useLocation } from 'react-router-dom';

export default function Header() {
  const location = useLocation();

  const isActive = (path: string) => {
    return location.pathname === path;
  };

  return (
    <header className="sticky top-0 z-50 select-none bg-[#0b0f19]/80 backdrop-blur-md border-b border-[#1e293b]">
      <div className="w-full max-w-[1700px] mx-auto flex items-center justify-between gap-4 px-4 sm:px-6 lg:px-8 py-3.5">
        {/* Logo */}
        <Link to="/" className="group flex items-center gap-2.5">
          <span className="grid size-9 place-items-center rounded-lg bg-indigo-600 text-white font-black text-lg transition-transform duration-300 group-hover:-rotate-6 shadow-[0_0_15px_rgba(99,102,241,0.4)]">
            D
          </span>
          <span className="flex flex-col leading-none">
            <span className="text-base font-bold tracking-tight text-white">DebugLab</span>
            <span className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold mt-0.5">Assessment Trainer</span>
          </span>
        </Link>

        {/* Navigation */}
        <nav className="hidden md:flex items-center gap-1 rounded-full border border-slate-800 bg-slate-900/50 p-1">
          <Link
            to="/"
            className={`rounded-full px-4 py-1.5 text-xs font-medium transition-all duration-200 ${
              isActive('/')
                ? 'bg-indigo-600 text-white shadow-[0_0_10px_rgba(99,102,241,0.3)]'
                : 'text-slate-400 hover:text-white hover:bg-slate-800/50'
            }`}
          >
            Dashboard
          </Link>
          <Link
            to="/problems"
            className={`rounded-full px-4 py-1.5 text-xs font-medium transition-all duration-200 ${
              isActive('/problems')
                ? 'bg-indigo-600 text-white shadow-[0_0_10px_rgba(99,102,241,0.3)]'
                : 'text-slate-400 hover:text-white hover:bg-slate-800/50'
            }`}
          >
            Problems
          </Link>
          <Link
            to="/setup"
            className={`rounded-full px-4 py-1.5 text-xs font-medium transition-all duration-200 ${
              isActive('/setup')
                ? 'bg-indigo-600 text-white shadow-[0_0_10px_rgba(99,102,241,0.3)]'
                : 'text-slate-400 hover:text-white hover:bg-slate-800/50'
            }`}
          >
            Configure Session
          </Link>
          <Link
            to="/progress"
            className={`rounded-full px-4 py-1.5 text-xs font-medium transition-all duration-200 ${
              isActive('/progress')
                ? 'bg-indigo-600 text-white shadow-[0_0_10px_rgba(99,102,241,0.3)]'
                : 'text-slate-400 hover:text-white hover:bg-slate-800/50'
            }`}
          >
            Progress
          </Link>
          <Link
            to="/settings"
            className={`rounded-full px-4 py-1.5 text-xs font-medium transition-all duration-200 ${
              isActive('/settings')
                ? 'bg-indigo-600 text-white shadow-[0_0_10px_rgba(99,102,241,0.3)]'
                : 'text-slate-400 hover:text-white hover:bg-slate-800/50'
            }`}
          >
            Settings
          </Link>
          <div className="h-4 w-px bg-slate-800 mx-1" />
          <Link
            to="/coding/setup"
            className={`rounded-full px-3.5 py-1.5 text-xs font-bold transition-all duration-200 flex items-center gap-1.5 ${
              location.pathname.startsWith('/coding')
                ? 'bg-gradient-to-r from-purple-600 to-indigo-600 text-white shadow-[0_0_12px_rgba(168,85,247,0.4)]'
                : 'text-purple-300 hover:text-white hover:bg-purple-950/40'
            }`}
          >
            <span className="size-1.5 rounded-full bg-purple-400 animate-pulse" />
            <span>AI Coding</span>
          </Link>
        </nav>

        {/* Live Indicator / Action */}
        <div className="flex items-center gap-2.5">
          <Link
            to="/coding/setup"
            className="inline-flex items-center gap-1.5 text-xs font-bold text-white bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 border border-purple-400/40 px-3.5 py-1.5 rounded-lg shadow-[0_0_15px_rgba(147,51,234,0.3)] transition-all active:scale-95"
          >
            <span>✨ AI Coding Assessment</span>
          </Link>
          <Link
            to="/problems"
            className="hidden lg:inline-flex items-center gap-1.5 text-xs font-bold text-indigo-300 hover:text-white bg-indigo-950/40 hover:bg-indigo-900/60 border border-indigo-800/50 px-3 py-1.5 rounded-lg transition-all"
          >
            Debugging Lab
          </Link>
          <span className="relative hidden sm:flex items-center gap-1.5 rounded-full border border-emerald-500/30 bg-emerald-500/10 px-3 py-1 text-[11px] font-bold text-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.15)]">
            <span className="relative flex size-2">
              <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-80"></span>
              <span className="relative inline-flex size-2 rounded-full bg-emerald-500"></span>
            </span>
            <span>ONLINE</span>
          </span>
        </div>
      </div>
    </header>
  );
}
