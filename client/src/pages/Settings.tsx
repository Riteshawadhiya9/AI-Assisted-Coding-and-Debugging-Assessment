import { useState, useEffect } from 'react';
import { 
  Settings as SettingsIcon, Sun, Moon, Sparkles, 
  Code2, Clock, Trash2, CheckCircle2, RotateCcw, 
  ShieldCheck
} from 'lucide-react';

export default function Settings() {
  // Theme state with lazy initialization
  const [theme, setTheme] = useState<'light' | 'dark'>(() => {
    return (localStorage.getItem('theme') as 'light' | 'dark') || 'dark';
  });

  // Editor states (persisted in localStorage for workspace loading)
  const [fontSize, setFontSize] = useState<number>(() => {
    return Number(localStorage.getItem('editor_font_size')) || 14;
  });

  const [wordWrap, setWordWrap] = useState<boolean>(() => {
    return localStorage.getItem('editor_word_wrap') !== 'false';
  });

  const [tabSize, setTabSize] = useState<number>(() => {
    return Number(localStorage.getItem('editor_tab_size')) || 4;
  });

  const [minimap, setMinimap] = useState<boolean>(() => {
    return localStorage.getItem('editor_minimap') === 'true';
  });

  const [timerAlerts, setTimerAlerts] = useState<boolean>(() => {
    return localStorage.getItem('setting_timer_alerts') !== 'false';
  });

  const [autoSubmit, setAutoSubmit] = useState<boolean>(() => {
    return localStorage.getItem('setting_auto_submit') !== 'false';
  });

  // Toast / notification state
  const [saveToast, setSaveToast] = useState<string | null>(null);

  const showNotification = (msg: string) => {
    setSaveToast(msg);
    setTimeout(() => {
      setSaveToast(null);
    }, 3000);
  };

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);

  const handleThemeChange = (newTheme: 'light' | 'dark') => {
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    showNotification(`Appearance changed to ${newTheme === 'dark' ? 'Dark' : 'Light'} Mode`);
  };

  const handleFontSizeChange = (size: number) => {
    setFontSize(size);
    localStorage.setItem('editor_font_size', String(size));
    showNotification(`Editor font size set to ${size}px`);
  };

  const handleWordWrapChange = (wrap: boolean) => {
    setWordWrap(wrap);
    localStorage.setItem('editor_word_wrap', String(wrap));
    showNotification(`Word wrap ${wrap ? 'enabled' : 'disabled'}`);
  };

  const handleTabSizeChange = (size: number) => {
    setTabSize(size);
    localStorage.setItem('editor_tab_size', String(size));
    showNotification(`Tab size set to ${size} spaces`);
  };

  const handleMinimapChange = (enabled: boolean) => {
    setMinimap(enabled);
    localStorage.setItem('editor_minimap', String(enabled));
    showNotification(`Minimap ${enabled ? 'enabled' : 'disabled'}`);
  };

  const handleTimerAlertsChange = (enabled: boolean) => {
    setTimerAlerts(enabled);
    localStorage.setItem('setting_timer_alerts', String(enabled));
    showNotification(`Timer warning alerts ${enabled ? 'enabled' : 'disabled'}`);
  };

  const handleAutoSubmitChange = (enabled: boolean) => {
    setAutoSubmit(enabled);
    localStorage.setItem('setting_auto_submit', String(enabled));
    showNotification(`Auto-submit on timeout ${enabled ? 'enabled' : 'disabled'}`);
  };

  const handleClearAttempts = () => {
    if (window.confirm('Are you sure you want to clear your local attempt history and progress stats?')) {
      localStorage.removeItem('debuglab_attempts');
      showNotification('Assessment attempt history cleared successfully');
    }
  };

  const handleResetDefaults = () => {
    if (window.confirm('Reset all editor and workspace settings to default values?')) {
      handleThemeChange('dark');
      handleFontSizeChange(14);
      handleWordWrapChange(true);
      handleTabSizeChange(4);
      handleMinimapChange(false);
      handleTimerAlertsChange(true);
      handleAutoSubmitChange(true);
      showNotification('Settings restored to defaults');
    }
  };

  return (
    <div className="w-full max-w-[1400px] px-4 sm:px-6 lg:px-8 py-8 relative z-10 space-y-8 mx-auto">
      {/* Title */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div className="space-y-1">
          <h1 className="text-3xl font-black tracking-tight text-white flex items-center gap-3">
            <SettingsIcon className="size-8 text-indigo-500" /> System Settings
          </h1>
          <p className="text-slate-400 text-sm">
            Configure Monaco code editor, appearance theme, assessment timer controls, and data storage.
          </p>
        </div>

        <button
          onClick={handleResetDefaults}
          className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 hover:text-white font-semibold text-xs transition-all cursor-pointer w-fit"
        >
          <RotateCcw className="size-3.5" />
          <span>Reset Defaults</span>
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Left Column: Core Editor & Appearance (col-span-7) */}
        <div className="lg:col-span-7 space-y-6">
          {/* 1. Theme Settings */}
          <div className="bg-[#111827]/70 border border-slate-800 rounded-2xl p-6 space-y-4 shadow-sm">
            <div className="flex items-center gap-2">
              <Sparkles className="size-4 text-indigo-400" />
              <h3 className="text-sm font-bold text-white uppercase tracking-wider">Appearance Theme</h3>
            </div>
            <p className="text-slate-400 text-xs leading-relaxed">
              Select standard visual mode for long coding and debugging reviews.
            </p>
            <div className="grid grid-cols-2 gap-4">
              <button
                onClick={() => handleThemeChange('dark')}
                className={`flex items-center justify-center gap-2 py-3.5 px-4 rounded-xl border text-xs font-bold transition-all cursor-pointer ${
                  theme === 'dark'
                    ? 'border-indigo-500 bg-indigo-500/15 text-white shadow-[0_0_15px_rgba(99,102,241,0.2)]'
                    : 'border-slate-800 bg-slate-900/40 text-slate-400 hover:border-slate-700'
                }`}
              >
                <Moon className="size-4 text-indigo-400" /> Dark Studio (Default)
              </button>
              <button
                onClick={() => handleThemeChange('light')}
                className={`flex items-center justify-center gap-2 py-3.5 px-4 rounded-xl border text-xs font-bold transition-all cursor-pointer ${
                  theme === 'light'
                    ? 'border-indigo-500 bg-indigo-500/15 text-white shadow-[0_0_15px_rgba(99,102,241,0.2)]'
                    : 'border-slate-800 bg-slate-900/40 text-slate-400 hover:border-slate-700'
                }`}
              >
                <Sun className="size-4 text-amber-400" /> Light Canvas
              </button>
            </div>
          </div>

          {/* 2. Monaco Editor Configuration */}
          <div className="bg-[#111827]/70 border border-slate-800 rounded-2xl p-6 space-y-5 shadow-sm">
            <div className="flex items-center gap-2">
              <Code2 className="size-4 text-indigo-400" />
              <h3 className="text-sm font-bold text-white uppercase tracking-wider">Monaco Code Editor</h3>
            </div>

            {/* Font Size */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 py-3 border-b border-slate-800/80">
              <div className="space-y-1">
                <h4 className="text-sm font-bold text-white">Font Size</h4>
                <p className="text-slate-400 text-xs">Set editor display text size in pixels.</p>
              </div>
              <div className="flex items-center gap-2">
                {[12, 14, 16, 18, 20].map((size) => (
                  <button
                    key={size}
                    onClick={() => handleFontSizeChange(size)}
                    className={`size-9 rounded-lg border text-xs font-bold transition-all cursor-pointer ${
                      fontSize === size
                        ? 'border-indigo-500 bg-indigo-600 text-white shadow-[0_0_10px_rgba(99,102,241,0.3)]'
                        : 'border-slate-800 bg-slate-900/50 text-slate-400 hover:border-slate-700'
                    }`}
                  >
                    {size}
                  </button>
                ))}
              </div>
            </div>

            {/* Soft Word Wrap */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 py-3 border-b border-slate-800/80">
              <div className="space-y-1">
                <h4 className="text-sm font-bold text-white">Soft Word Wrap</h4>
                <p className="text-slate-400 text-xs">Wrap long code statements within the Monaco viewport.</p>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={() => handleWordWrapChange(true)}
                  className={`px-4 py-1.5 rounded-lg border text-xs font-bold transition-all cursor-pointer ${
                    wordWrap === true
                      ? 'border-indigo-500 bg-indigo-600 text-white'
                      : 'border-slate-800 bg-slate-900/50 text-slate-400 hover:border-slate-700'
                  }`}
                >
                  On
                </button>
                <button
                  onClick={() => handleWordWrapChange(false)}
                  className={`px-4 py-1.5 rounded-lg border text-xs font-bold transition-all cursor-pointer ${
                    wordWrap === false
                      ? 'border-indigo-500 bg-indigo-600 text-white'
                      : 'border-slate-800 bg-slate-900/50 text-slate-400 hover:border-slate-700'
                  }`}
                >
                  Off
                </button>
              </div>
            </div>

            {/* Tab Size */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 py-3 border-b border-slate-800/80">
              <div className="space-y-1">
                <h4 className="text-sm font-bold text-white">Tab Indentation</h4>
                <p className="text-slate-400 text-xs">Number of spaces per indentation level.</p>
              </div>
              <div className="flex items-center gap-2">
                {[2, 4].map((size) => (
                  <button
                    key={size}
                    onClick={() => handleTabSizeChange(size)}
                    className={`px-4 py-1.5 rounded-lg border text-xs font-bold transition-all cursor-pointer ${
                      tabSize === size
                        ? 'border-indigo-500 bg-indigo-600 text-white'
                        : 'border-slate-800 bg-slate-900/50 text-slate-400 hover:border-slate-700'
                    }`}
                  >
                    {size} Spaces
                  </button>
                ))}
              </div>
            </div>

            {/* Minimap */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 py-3">
              <div className="space-y-1">
                <h4 className="text-sm font-bold text-white">Code Minimap</h4>
                <p className="text-slate-400 text-xs">Show graphical overview scrollbar preview in editor.</p>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={() => handleMinimapChange(true)}
                  className={`px-4 py-1.5 rounded-lg border text-xs font-bold transition-all cursor-pointer ${
                    minimap === true
                      ? 'border-indigo-500 bg-indigo-600 text-white'
                      : 'border-slate-800 bg-slate-900/50 text-slate-400 hover:border-slate-700'
                  }`}
                >
                  Visible
                </button>
                <button
                  onClick={() => handleMinimapChange(false)}
                  className={`px-4 py-1.5 rounded-lg border text-xs font-bold transition-all cursor-pointer ${
                    minimap === false
                      ? 'border-indigo-500 bg-indigo-600 text-white'
                      : 'border-slate-800 bg-slate-900/50 text-slate-400 hover:border-slate-700'
                  }`}
                >
                  Hidden
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column: Assessment Timers, Sandbox & Storage (col-span-5) */}
        <div className="lg:col-span-5 space-y-6">
          {/* 3. Assessment & Timing Controls */}
          <div className="bg-[#111827]/70 border border-slate-800 rounded-2xl p-6 space-y-4 shadow-sm">
            <div className="flex items-center gap-2">
              <Clock className="size-4 text-indigo-400" />
              <h3 className="text-sm font-bold text-white uppercase tracking-wider">Exam & Timer Controls</h3>
            </div>

            <div className="space-y-3 text-xs">
              <div className="flex items-center justify-between p-3.5 bg-slate-900/50 border border-slate-800 rounded-xl">
                <div>
                  <div className="font-bold text-white">Timer Alerts (10m, 5m, 1m)</div>
                  <div className="text-slate-400 text-[11px]">Show notification banners during timed exams</div>
                </div>
                <button
                  onClick={() => handleTimerAlertsChange(!timerAlerts)}
                  className={`px-3 py-1 rounded-lg font-bold border text-xs cursor-pointer ${
                    timerAlerts 
                      ? 'bg-emerald-950/30 border-emerald-500/40 text-emerald-400' 
                      : 'bg-slate-900 border-slate-800 text-slate-500'
                  }`}
                >
                  {timerAlerts ? 'Active' : 'Muted'}
                </button>
              </div>

              <div className="flex items-center justify-between p-3.5 bg-slate-900/50 border border-slate-800 rounded-xl">
                <div>
                  <div className="font-bold text-white">Auto-Submit on Timeout</div>
                  <div className="text-slate-400 text-[11px]">Automatically evaluate solution when time expires</div>
                </div>
                <button
                  onClick={() => handleAutoSubmitChange(!autoSubmit)}
                  className={`px-3 py-1 rounded-lg font-bold border text-xs cursor-pointer ${
                    autoSubmit 
                      ? 'bg-emerald-950/30 border-emerald-500/40 text-emerald-400' 
                      : 'bg-slate-900 border-slate-800 text-slate-500'
                  }`}
                >
                  {autoSubmit ? 'Enabled' : 'Disabled'}
                </button>
              </div>
            </div>
          </div>

          {/* 4. Local Execution Sandbox Status */}
          <div className="bg-[#111827]/70 border border-slate-800 rounded-2xl p-6 space-y-4 shadow-sm">
            <div className="flex items-center gap-2">
              <ShieldCheck className="size-4 text-emerald-400" />
              <h3 className="text-sm font-bold text-white uppercase tracking-wider">Engine Status</h3>
            </div>

            <div className="space-y-2.5 font-mono text-xs">
              <div className="flex items-center justify-between p-3 bg-slate-900/60 border border-slate-800 rounded-xl">
                <span className="text-slate-400">Sandbox Provider</span>
                <span className="text-emerald-400 font-bold flex items-center gap-1.5">
                  <span className="size-2 rounded-full bg-emerald-400 animate-pulse"></span>
                  Deterministic Mock
                </span>
              </div>
              <div className="flex items-center justify-between p-3 bg-slate-900/60 border border-slate-800 rounded-xl">
                <span className="text-slate-400">Question Bank</span>
                <span className="text-white font-bold">40 Local DSA Questions</span>
              </div>
              <div className="flex items-center justify-between p-3 bg-slate-900/60 border border-slate-800 rounded-xl">
                <span className="text-slate-400">External Dependencies</span>
                <span className="text-indigo-400 font-bold">None (Offline Ready)</span>
              </div>
            </div>
          </div>

          {/* 5. Data Storage Management */}
          <div className="bg-[#111827]/70 border border-slate-800 rounded-2xl p-6 space-y-4 shadow-sm">
            <div className="flex items-center gap-2">
              <Trash2 className="size-4 text-rose-400" />
              <h3 className="text-sm font-bold text-white uppercase tracking-wider">Local Storage</h3>
            </div>
            <p className="text-slate-400 text-xs leading-relaxed">
              Clear your recorded assessment scores, diagnosis history, and solved problem markers.
            </p>
            <button
              onClick={handleClearAttempts}
              className="w-full py-2.5 rounded-xl border border-rose-500/30 bg-rose-950/20 hover:bg-rose-900/30 text-rose-300 font-bold text-xs transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              <Trash2 className="size-3.5" /> Clear All Assessment Records
            </button>
          </div>
        </div>
      </div>

      {/* Floating Save Toast Notification */}
      {saveToast && (
        <div className="fixed bottom-6 right-6 z-50 bg-indigo-600 border border-indigo-400 text-white rounded-xl py-3 px-5 flex items-center gap-2.5 shadow-2xl animate-fade-in font-semibold text-xs">
          <CheckCircle2 className="size-4 text-white" />
          <span>{saveToast}</span>
        </div>
      )}
    </div>
  );
}
