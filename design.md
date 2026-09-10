# Debugging Assessment Trainer --- UI/UX Design

## 1. Design Objective

The interface should feel like a professional coding assessment
environment, not a generic chatbot.

Primary qualities:

-   focused
-   fast
-   readable
-   low distraction
-   keyboard-friendly
-   professional
-   assessment-oriented

The user should be able to understand the question and start debugging
within seconds.

## 2. Visual Direction

Use a modern developer-tool aesthetic.

Recommended:

-   dark editor area
-   light or dark application shell based on user preference
-   strong blue accent
-   subtle borders
-   restrained shadows
-   compact spacing
-   clear typography
-   no excessive gradients
-   no distracting animations

Use responsive design, but optimize primarily for desktop because the
assessment is code-heavy.

## 3. Main Dashboard

Header:

``` text
DebugLab
Stage 3 Debugging Trainer
```

Main cards:

``` text
┌─────────────────────────────────────────────┐
│ Start Debugging Assessment                  │
│ 1 Question • 20 Minutes • C/C++/Java       │
│                                             │
│              [ Start Exam ]                 │
└─────────────────────────────────────────────┘
```

Additional cards:

-   Practice by Topic
-   Weak Areas
-   Recent Attempts
-   Current Accuracy
-   Average Debugging Time

## 4. Practice Setup

Controls:

``` text
Language
[ C ] [ C++ ] [ Java ]

Topic
[ Random ▼ ]

Difficulty
[ Easy ] [ Medium ] [ Hard ]

Mode
[ Practice ] [ Exam ]
```

Primary button:

``` text
Start Debugging
```

Show a short description:

``` text
You will receive intentionally buggy code.
Your goal is to understand the intended algorithm,
find the bug, fix it, and validate your solution.
```

## 5. Debugging Workspace

Recommended structure:

``` text
┌─────────────────────────────────────────────────────────────┐
│ Question 12     Graphs • Hard     C++       19:42 remaining │
├───────────────────────┬───────────────────────┬─────────────┤
│ Problem               │ Code Editor           │ AI / Tests  │
│                       │                       │             │
│ Statement             │ 1  #include...       │ Test Cases  │
│ Constraints           │ 2  ...                │             │
│ Examples              │ 3  ...                │             │
│                       │                       │             │
│                       │                       │             │
│                       │                       │             │
├───────────────────────┴───────────────────────┴─────────────┤
│ Console / Output / Compilation Result                       │
├─────────────────────────────────────────────────────────────┤
│ Review → Identify → Fix → Validate        [Submit Solution] │
└─────────────────────────────────────────────────────────────┘
```

## 6. Step Indicator

Use four connected stages:

``` text
● Review ─── ● Identify ─── ● Fix ─── ● Validate
```

The current stage should be highlighted.

Do not make these stages unnecessarily restrictive. A user may go back
and forth while debugging.

## 7. Problem Panel

Show:

-   title
-   problem statement
-   constraints
-   examples
-   expected behavior
-   input/output description

Do not reveal:

-   bug location
-   bug type
-   correct code
-   final solution

until submission in Exam Mode.

## 8. Code Editor

Use Monaco Editor.

Required:

-   line numbers
-   syntax highlighting
-   minimap toggle
-   search
-   keyboard shortcuts
-   editable source
-   reset button
-   font-size controls
-   word wrapping toggle

Default editor font size:

``` text
14–15px
```

## 9. Test/Console Panel

Tabs:

``` text
Tests | Console | Compilation
```

Each test should display:

``` text
Test 1
Input:
...

Expected:
...

Actual:
...

✓ Passed
```

or:

``` text
✗ Failed
```

Compilation errors should be shown clearly with source-line references
when possible.

## 10. AI Assistant

The AI assistant is optional.

Modes:

``` text
Hint
Explain Error
Review My Reasoning
Explain After Submission
```

Important Exam Mode rule:

-   before submission, AI must not reveal the exact bug or corrected
    code
-   hints should be configurable
-   after submission, the assistant can explain everything

Example pre-submit hint:

``` text
Your traversal looks reasonable.
Check what happens when the graph contains a node
that was already visited.
```

Avoid:

``` text
Change visited[node] = true to visited[node] = false.
```

## 11. Submission Result

After submission:

``` text
┌───────────────────────────────────────────────┐
│ Result: Needs Improvement                    │
│                                               │
│ Tests Passed: 8 / 10                         │
│ Time: 13m 42s                                │
│ Score: 72%                                    │
│                                               │
│ Primary Bug: Incorrect visited-state logic   │
│                                               │
│ [View Explanation] [Try Similar Question]    │
└───────────────────────────────────────────────┘
```

For a successful attempt:

``` text
✓ All hidden tests passed
```

## 12. Explanation Screen

Structure:

1.  What the problem asked
2.  What was wrong
3.  Why it was wrong
4.  Corrected logic
5.  Edge cases
6.  Complexity
7.  How to recognize this bug next time

The final section is important for interview preparation.

## 13. Progress Dashboard

Display:

-   total questions attempted
-   solved
-   failed
-   accuracy
-   average time
-   average score
-   strongest topics
-   weakest topics
-   recent mistakes

Example:

``` text
Graphs       62%
Trees        78%
2D DP        49%
Binary Search 71%
```

Use weak-topic detection to recommend the next question.

## 14. Responsive Behavior

Desktop:

-   three-column workspace

Tablet:

-   two-column layout
-   collapsible AI panel

Mobile:

-   stacked panels
-   editor remains usable
-   exam mode should display a warning that desktop is recommended

## 15. Accessibility

Support:

-   keyboard navigation
-   sufficient contrast
-   visible focus states
-   semantic buttons
-   ARIA labels where needed
-   reduced motion preference

## 16. Performance

The workspace must feel instant.

Avoid:

-   unnecessary rerenders of Monaco
-   rebuilding the editor on every keystroke
-   large client-side question payloads
-   excessive animation

Persist editor content in memory during the attempt and save only useful
checkpoints.

## 17. UX Rules for Exam Simulation

Never:

-   reset the timer after refresh without an explicit policy
-   reveal hidden tests
-   reveal bug metadata before submission
-   show the correct solution during the exam
-   allow the AI to directly solve the question

Always:

-   show remaining time
-   make Run easy to access
-   make Submit obvious
-   warn before final submission
-   auto-submit at zero
