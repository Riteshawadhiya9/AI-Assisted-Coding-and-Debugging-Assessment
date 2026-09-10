import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import BackgroundGrid from './components/BackgroundGrid';
import Dashboard from './pages/Dashboard';
import Problems from './pages/Problems';
import PracticeSetup from './pages/PracticeSetup';
import Workspace from './pages/Workspace';
import Results from './pages/Results';
import Progress from './pages/Progress';
import Settings from './pages/Settings';
import CodingSetup from './pages/CodingSetup';
import CodingWorkspace from './pages/CodingWorkspace';
import CodingResults from './pages/CodingResults';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-[#0b0f19] text-slate-100 flex flex-col relative overflow-hidden">
        {/* Background design accents */}
        <BackgroundGrid />
        
        {/* Navigation bar */}
        <Header />
        
        {/* Content routing viewports */}
        <main className="flex-1 relative z-10 flex flex-col w-full">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/problems" element={<Problems />} />
            <Route path="/setup" element={<PracticeSetup />} />
            <Route path="/workspace" element={<Workspace />} />
            <Route path="/results" element={<Results />} />
            <Route path="/progress" element={<Progress />} />
            <Route path="/settings" element={<Settings />} />

            {/* AI-Assisted Coding Assessment Routes */}
            <Route path="/coding" element={<CodingSetup />} />
            <Route path="/coding/setup" element={<CodingSetup />} />
            <Route path="/coding/workspace" element={<CodingWorkspace />} />
            <Route path="/coding/results" element={<CodingResults />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
