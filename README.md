# Debugging Assessment Trainer (DebugLab) - Phase 1 MVP

A browser-based debugging practice platform built to simulate a Capgemini-style Stage 3 Debugging Assessment.

## Project Goal
Improve debugging speed, logic identification, and edge-case validation across C, C++, and Java. Emphasizes advanced Data Structures and Algorithms (DSA) like Trees, Graphs, and 2D Dynamic Programming.

---

## 1. Directory Structure

```text
debugging-assessment-trainer/
├── client/                     # Frontend (React + Vite + TS + Tailwind CSS v4)
│   ├── src/
│   │   ├── components/         # Navigation header, background grid styles
│   │   ├── pages/              # Routing panels (Dashboard, Setup, Workspace, Results, etc.)
│   │   ├── types/              # Type definitions (Questions, Attempts, TestCase)
│   │   ├── App.tsx             # Route declarations
│   │   └── index.css           # Premium theme variables and Tailwind directives
├── server/                     # Backend (Node.js + Express + TS)
│   ├── src/
│   │   ├── controllers/        # Request controllers
│   │   ├── routes/             # API routes (/api/questions, /api/health)
│   │   ├── services/           # Question loader service
│   │   ├── data/               # Seed questions database (questions.json)
│   │   └── app.ts              # Entrypoint Express app configuration
├── package.json                # Root package configuration
└── README.md
```

---

## 2. Quick Start & Setup

### Prerequisites
Make sure you have **Node.js (v18+)** and **npm** installed.

### Setup and Running locally

You can easily launch the frontend and backend in development mode by running them in separate terminal instances or processes.

#### Step 1: Start the Backend Server
```bash
cd server
npm install
npm run dev
```
The server will start on [http://localhost:5000](http://localhost:5000).

#### Step 2: Start the Frontend Client
```bash
cd client
npm install
npm run dev
```
The Vite development server will start on [http://localhost:5173](http://localhost:5173) with automated API proxies configured.

---

## 3. Initial Features Implemented (Phase 1)
- **Sticky Frosted Header:** With rotating brand box and active link tracers.
- **Glowing Abstract Grid:** Modern developer dashboard layout styling inspired by knowvy.xyz.
- **Dashboard:** Snapshot statistics, rapid topic selectors, and recent attempt logs.
- **Practice Configuration:** Custom selectors for languages (C/C++/Java), topics (Trees, Graphs, DP), difficulties, and timer modes.
- **Debugging Workspace:** Integrated Monaco Code Editor, step workflow tracking (Review → Identify → Fix → Validate), visible/hidden test case tabs, simulated compilation consoles, and logical hints.
- **Explanation Review:** Side-by-side buggy/correct code snippets, expected complexities, and bug descriptions.
- **Progress Tracking:** Performance metrics (accuracy, solved vs attempted) and history logs.
