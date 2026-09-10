# Debugging Assessment Trainer --- Architecture

## 1. Architecture Decision

Use a lightweight MERN-style architecture:

-   Frontend: React + Vite + TypeScript
-   UI: Tailwind CSS
-   Code editor: Monaco Editor
-   Backend: Node.js + Express + TypeScript
-   Database: MongoDB, optional for MVP
-   Code execution: Judge0 adapter
-   AI: Groq/Mistral adapter
-   Local MVP persistence: localStorage

The backend is intentionally small. It is required mainly to protect API
keys and proxy external services safely.

## 2. High-Level Flow

``` text
                 ┌──────────────────────────┐
                 │       React Frontend     │
                 │                          │
                 │ Dashboard                │
                 │ Practice Setup           │
                 │ Debugging Workspace      │
                 │ Monaco Editor            │
                 │ Results                  │
                 │ AI Chat                  │
                 └────────────┬─────────────┘
                              │ HTTP
                              ▼
                 ┌──────────────────────────┐
                 │      Express Backend     │
                 │                          │
                 │ /api/questions           │
                 │ /api/execute             │
                 │ /api/ai                  │
                 │ /api/attempts            │
                 └───────┬─────────┬────────┘
                         │         │
                ┌────────▼───┐ ┌──▼────────────┐
                │   Judge0    │ │ Groq/Mistral │
                │ Code Runner │ │ AI Provider  │
                └─────────────┘ └──────────────┘
                         │
                         ▼
                    ┌──────────┐
                    │ MongoDB  │
                    │ optional │
                    └──────────┘
```

## 3. Why Backend Is Still Useful

A frontend-only application is possible for static questions, but it
creates two important problems:

1.  Groq/Mistral API keys would be exposed to the browser.
2.  C/C++/Java cannot safely be compiled and executed directly in a
    normal browser environment.

Therefore use a minimal Express backend.

Do not build a large backend.

## 4. Suggested Repository

``` text
debugging-assessment-trainer/
│
├── client/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── features/
│   │   │   ├── practice/
│   │   │   ├── exam/
│   │   │   ├── editor/
│   │   │   ├── questions/
│   │   │   ├── results/
│   │   │   └── ai/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── store/
│   │   ├── types/
│   │   └── utils/
│   └── package.json
│
├── server/
│   ├── src/
│   │   ├── controllers/
│   │   ├── routes/
│   │   ├── services/
│   │   │   ├── execution/
│   │   │   └── ai/
│   │   ├── providers/
│   │   ├── validators/
│   │   ├── models/
│   │   ├── middleware/
│   │   └── app.ts
│   └── package.json
│
├── data/
│   └── questions/
│
├── docs/
│
├── .env.example
├── README.md
├── architecture.md
├── design.md
├── phases.md
└── PRD.md
```

## 5. Core Backend Modules

### QuestionService

Responsibilities:

-   load seed questions
-   filter by language/topic/difficulty
-   select random question
-   validate question structure

### ExecutionService

Interface:

``` text
execute(code, language, stdin, expectedOutput?)
```

Implementation:

``` text
Judge0ExecutionProvider
```

Never put Judge0 credentials in React.

### AIService

Interface:

``` text
generateQuestion()
generateHint()
explainBug()
reviewAttempt()
```

Implement:

``` text
GroqProvider
MistralProvider
```

Use environment configuration to choose provider.

### AttemptService

Responsibilities:

-   create attempt
-   record runs
-   record submission
-   calculate score
-   store history

For MVP this can use localStorage on the client. Build the service
interface now so MongoDB can be added later.

## 6. API Design

### GET /api/health

Returns:

``` json
{
  "ok": true
}
```

### GET /api/questions/random

Query parameters:

``` text
language=C
topic=graphs
difficulty=hard
```

### POST /api/questions/generate

Used by AI question generation.

### POST /api/execute

Request:

``` json
{
  "language": "cpp",
  "code": "...",
  "stdin": "...",
  "expectedOutput": "..."
}
```

Response:

``` json
{
  "status": "accepted",
  "stdout": "...",
  "stderr": null,
  "compileOutput": null,
  "time": "0.02",
  "memory": 12000
}
```

### POST /api/ai/hint

### POST /api/ai/explain

### POST /api/ai/review

## 7. Security

Never:

-   execute arbitrary code directly with Node child_process
-   expose Groq/Mistral/Judge0 secrets in VITE\_ variables
-   trust client-provided scores
-   trust AI-generated correctness claims
-   allow unlimited execution requests

Use:

-   execution timeouts
-   memory limits
-   request validation
-   rate limiting
-   payload-size limits
-   CORS configuration
-   environment variables
-   server-side score calculation where persistent attempts are enabled

## 8. Question Validation Pipeline

AI-generated question:

``` text
LLM
 ↓
JSON schema validation
 ↓
Code extraction
 ↓
Correct-code execution
 ↓
Buggy-code execution
 ↓
Test verification
 ↓
Consistency check
 ↓
Store only if valid
```

If validation fails:

``` text
discard question
```

Never silently store an unvalidated AI question.

## 9. Frontend State

Suggested state:

``` text
question
language
code
originalCode
activeStep
timer
runResults
submissionResult
attempt
hintsUsed
isSubmitting
```

Use React state/context first.

Do not add Redux unless the application actually becomes difficult to
manage.

## 10. Timer Architecture

Store:

``` text
startedAt
deadline
remainingMs
```

Compute remaining time from:

``` text
deadline - Date.now()
```

This avoids incorrect timing caused by browser throttling.

## 11. Execution Strategy

Use visible tests for quick feedback.

Use hidden tests during final validation.

A run should return:

-   compilation status
-   stdout
-   stderr
-   runtime
-   memory
-   test result

Final submission should execute all hidden tests.

## 12. Deployment Strategy

Development:

``` text
React localhost:5173
Express localhost:5000
```

Production can be:

``` text
Frontend → Vercel/Netlify
Backend → Render/Railway/Fly.io/etc.
MongoDB → MongoDB Atlas
Judge0 → hosted/self-hosted instance
```

The exact hosting provider is not part of the MVP architecture.

## 13. Important Implementation Principle

Build the application so the execution and AI providers are replaceable.

Do not couple React directly to Groq, Mistral, or Judge0.

Use:

``` text
React
  ↓
Express service
  ↓
Provider interface
  ↓
Groq / Mistral / Judge0
```

This makes switching providers easy.
