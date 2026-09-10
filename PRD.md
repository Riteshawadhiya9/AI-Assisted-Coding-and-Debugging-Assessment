# Debugging Assessment Trainer --- PRD

## 1. Product Goal

Build a browser-based debugging practice platform that simulates a
Capgemini-style Stage 3 Debugging Assessment.

The target practice format is:

-   1 debugging question
-   approximately 20 minutes
-   supported languages: C, C++, Java
-   advanced DSA emphasis
-   user must review, identify, fix, and validate buggy code
-   primary topics: Trees, Graphs, 2D Dynamic Programming, and other
    advanced DSA
-   the application should feel like a real assessment rather than a
    generic coding website

The application is for intensive interview/assessment preparation, so
correctness and realistic debugging questions are more important than
unnecessary features.

## 2. Core User Modes

### Practice Mode

The user can:

-   select a language
-   select a topic or use Random
-   select difficulty
-   receive one buggy program
-   inspect the problem statement
-   inspect the code
-   edit the code
-   run the code
-   see compiler/runtime/test results
-   submit a fix
-   receive an explanation of the bug
-   see the correct approach
-   see complexity
-   move to another question

Hints should be optional and should reduce the practice value if used.

### Exam Mode

Exam Mode must simulate the target assessment:

-   exactly one question
-   20-minute countdown
-   C/C++/Java
-   no solution shown before submission
-   no answer explanation before final submission
-   optional "Run" functionality
-   final submission freezes the attempt
-   show score/report after submission
-   record time taken
-   show bugs found/fixed and validation result

## 3. Debugging Workflow

The UI must explicitly communicate the four-step workflow:

1.  Review
    -   Read problem statement and code.
2.  Identify
    -   Locate logical, syntax, runtime, or algorithmic problems.
3.  Fix
    -   Modify the code.
4.  Validate
    -   Run visible and hidden tests and check edge cases.

The UI should visually indicate the current stage without forcing the
user into separate screens.

## 4. Question Model

Each question should contain:

-   id
-   title
-   problemStatement
-   language
-   topic
-   subtopic
-   difficulty
-   estimatedTime
-   buggyCode
-   correctCode
-   bugList
-   primaryBugType
-   explanation
-   intendedApproach
-   constraints
-   visibleTestCases
-   hiddenTestCases
-   expectedComplexity
-   tags

Bug types:

-   syntax
-   compilation
-   runtime
-   logical
-   boundary
-   off-by-one
-   incorrect condition
-   incorrect initialization
-   incorrect recursion
-   incorrect traversal
-   incorrect state transition
-   incorrect data structure usage
-   time complexity
-   memory/overflow
-   edge case

## 5. Important Quality Rule

Every generated question must be validated.

A question is valid only if:

1.  The correct code compiles/runs.
2.  The buggy code demonstrates the intended failure or incorrect
    behavior.
3.  The stated test cases actually expose the bug when appropriate.
4.  The explanation matches the actual code.
5.  The intended solution matches the problem statement.
6.  The expected complexity is accurate.

Never trust an LLM-generated debugging question blindly.

Use a deterministic seed question bank as the fallback if AI generation
fails.

## 6. Initial Topic Coverage

Prioritize:

### Trees

-   BST
-   binary tree traversal
-   height/depth
-   lowest common ancestor
-   diameter
-   recursion errors
-   iterative traversal bugs
-   subtree/state bugs

### Graphs

-   BFS
-   DFS
-   connected components
-   cycle detection
-   shortest path
-   topological sort
-   visited-array mistakes
-   adjacency-list mistakes

### 2D Dynamic Programming

-   grid paths
-   minimum path sum
-   obstacle grid
-   matrix DP
-   incorrect state transition
-   row/column initialization bugs

### Advanced DSA

-   binary search on answer
-   heaps/priority queues
-   sliding window
-   prefix sums
-   monotonic stack
-   backtracking
-   greedy
-   hashing
-   recursion
-   sorting
-   two pointers

## 7. Difficulty

Three levels:

### Easy

One obvious bug, simple algorithm.

### Medium

One or two subtle bugs, moderate DSA.

### Hard

Subtle logical/edge-case bug, advanced DSA, code that looks mostly
correct.

Target distribution for the first 100 questions:

-   Easy: 20
-   Medium: 50
-   Hard: 30

## 8. Scoring

Practice mode:

-   Bug identified: 30%
-   Correct fix: 40%
-   Visible tests: 10%
-   Hidden tests: 10%
-   Edge-case validation: 10%

Exam mode:

-   Correctness: 70%
-   Bug diagnosis: 20%
-   Efficiency/complexity: 10%

The exact scoring can be configurable.

## 9. Timer

Exam Mode:

-   20:00 countdown
-   warning at 10:00
-   warning at 05:00
-   warning at 01:00
-   auto-submit at 00:00

The timer must use a timestamp-based implementation, not repeated
decrement logic alone, so browser tab throttling does not incorrectly
extend the exam.

## 10. Code Execution

The application needs a sandboxed code execution service because
browsers cannot safely compile and execute arbitrary C/C++/Java code
themselves.

Preferred architecture:

Browser → Express API → Judge0 → result

Judge0 supports sandboxed compilation/execution and detailed execution
results.

Never expose execution-service credentials in frontend code.

The execution provider must be implemented behind an interface so Judge0
can later be replaced with another provider or a self-hosted runner.

## 11. AI Assistant

The chatbot is not the main assessment engine.

Use AI for:

-   generating additional debugging questions
-   generating explanations
-   generating hints
-   explaining compiler/runtime output
-   reviewing the user's debugging reasoning
-   creating targeted follow-up questions

Do NOT use AI as the sole source of truth for whether code is correct.

Use an AI provider abstraction:

AIProvider - generateQuestion() - explainBug() - generateHint() -
reviewAttempt()

Providers:

-   Groq
-   Mistral

The API key stays on the backend.

## 12. Persistence

MVP:

-   localStorage for settings and practice history
-   no authentication required

Later:

-   MongoDB
-   user accounts
-   persistent attempts
-   topic-wise analytics
-   streaks
-   weak-topic detection

Do not block the MVP on authentication or MongoDB.

## 13. Main Screens

1.  Dashboard
2.  Practice Setup
3.  Debugging Workspace
4.  Submission/Result
5.  Progress/Analytics
6.  Settings
7.  AI Chat Panel

## 14. Debugging Workspace Layout

Recommended desktop layout:

-   top bar: question, language, difficulty, timer
-   left panel: problem statement, constraints, examples
-   center: Monaco code editor
-   right/bottom panel: test cases, console, AI assistant
-   bottom status: compile/run result
-   top or side step indicator: Review → Identify → Fix → Validate

The code editor must support:

-   syntax highlighting
-   line numbers
-   autocomplete where practical
-   search
-   formatting
-   reset code
-   keyboard shortcuts
-   theme suitable for long coding sessions

## 15. Non-Goals for MVP

Do not initially build:

-   social profiles
-   leaderboards
-   payments
-   complex authentication
-   admin dashboard
-   real-time multiplayer
-   mobile-native application
-   elaborate animations

The goal is to get a reliable debugging simulator running as quickly as
possible.

## 16. Success Criteria

The MVP is successful when the user can:

1.  Open the app.
2.  Select C, C++, or Java.
3.  Start a 20-minute debugging question.
4.  Read the problem.
5.  Edit buggy code.
6.  Run it.
7.  See compiler/runtime/test feedback.
8.  Fix the code.
9.  Submit it.
10. See whether it passes.
11. Read the explanation afterward.
12. Start another question.
13. Review weak topics and previous attempts.

## 17. Engineering Priorities

Priority order:

1.  Correct debugging questions
2.  Reliable code execution
3.  Fast debugging workspace
4.  Exam-mode timer and submission
5.  AI assistance
6.  Analytics
7.  Visual polish
