export type Language = 'c' | 'cpp' | 'java';

export type Difficulty = 'easy' | 'medium' | 'hard';

export type Topic = 
  // Primary Categories
  | 'arrays'
  | 'strings'
  | 'hashmap'
  | 'trees'
  | 'recursion'
  | 'dp'
  | '2ddp'
  | 'graphs'
  | 'advanced-dsa'
  | 'random'
  // Sub-topics & Aliases
  | 'bst'
  | 'binary-tree'
  | 'bfs'
  | 'dfs'
  | 'shortest-path'
  | 'topological-sort'
  | 'matrix-dp'
  | 'knapsack-01'
  | 'lcs'
  | 'lis'
  | 'binary-search'
  | 'heap'
  | 'monotonic-stack'
  | 'sliding-window'
  | 'two-pointers'
  | 'prefix-sum'
  | 'linked-list'
  | 'backtracking';

export type BugType =
  | 'syntax'
  | 'compilation'
  | 'runtime'
  | 'logical'
  | 'boundary'
  | 'off-by-one'
  | 'incorrect condition'
  | 'incorrect initialization'
  | 'incorrect recursion'
  | 'incorrect traversal'
  | 'incorrect state transition'
  | 'incorrect data structure usage'
  | 'time complexity'
  | 'integer overflow'
  | 'edge case';

export interface VisualData {
  type: 'tree' | 'graph' | 'matrix' | 'linkedList' | 'array' | 'blocks';
  title?: string;
  data: any;
}

export interface TestCase {
  id: number;
  input: string;
  expectedOutput: string;
  isHidden: boolean;
  actualOutput?: string;
  passed?: boolean;
  visualData?: VisualData;
  explanation?: string;
}

export interface Bug {
  id: number;
  description: string;
  type: BugType;
  lineRange?: string;
}

export interface LanguageImplementation {
  buggyCode: string;
  correctCode?: string;
}

export interface Question {
  id: string;
  title: string;
  problemStatement: string;
  topic: Topic;
  subtopic: string;
  difficulty: Difficulty;
  estimatedTime: number;
  bugType?: BugType;
  primaryBugType?: BugType;
  bugConcept?: string;
  explanation?: string;
  intendedApproach: string;
  constraints: string[];
  examples?: TestCase[];
  visibleTestCases: TestCase[];
  hiddenTestCases: TestCase[];
  expectedComplexity: {
    time: string;
    space: string;
  };
  tags: string[];
  visualData?: VisualData;
  implementations: {
    c: LanguageImplementation;
    cpp: LanguageImplementation;
    java: LanguageImplementation;
  };
  // Active/selected language helper fields
  language?: Language;
  buggyCode?: string;
  correctCode?: string;
  bugList?: Bug[];
}

export interface UserDiagnosis {
  bugType: BugType | '';
  notes: string;
  isLocked: boolean;
}

export interface RunHistoryItem {
  id: number;
  timestamp: string;
  passed: boolean;
  passedCount: number;
  totalCount: number;
  compileOutput: string;
  runtimeOutput: string;
  executionTimeMs: number;
}

export interface ScoreBreakdown {
  correctness: number;
  tests: number;
  diagnosis: number;
  timeBonus: number;
  hintsPenalty: number;
  finalScore: number;
}

export interface Attempt {
  id: string;
  questionId: string;
  questionTitle: string;
  language: Language;
  difficulty: Difficulty;
  topic: Topic;
  mode: 'practice' | 'exam';
  score: number;
  timeSpentSeconds: number;
  status: 'passed' | 'failed' | 'in_progress';
  date: string;
  codeSubmitted: string;
  bugsDiagnosed: string[];
  diagnosedBugType?: string;
  diagnosisNotes?: string;
  diagnosisCorrect?: boolean;
  scoreBreakdown?: ScoreBreakdown;
  testsPassed: number;
  totalTests: number;
}

export interface Analytics {
  totalAttempted: number;
  totalSolved: number;
  averageScore: number;
  averageTimeSeconds: number;
  accuracy: number;
  topicAccuracy: Record<Topic, number>;
  difficultyCount: Record<Difficulty, number>;
}

// ==========================================
// AI-ASSISTED CODING SECTION TYPES
// ==========================================

export type CodingLanguage = 'python' | 'javascript' | 'typescript' | 'java' | 'cpp';

export interface CodingExample {
  input: string;
  output: string;
  explanation?: string;
}

export interface CodingTestCase {
  id: number;
  input: string;
  expectedOutput: string;
  explanation?: string;
  actualOutput?: string;
  passed?: boolean;
  isHidden?: boolean;
}

export interface CodingQuestion {
  id: string;
  number?: number;
  title: string;
  difficulty: string;
  topic: string;
  description?: string;
  problemStatement?: string;
  examples: CodingExample[];
  constraints: string[];
  starterCode: Record<string, string>;
  solutionCode?: Record<string, string>;
  testCases?: CodingTestCase[];
  visibleTestCases?: CodingTestCase[];
  hiddenTestCases?: CodingTestCase[];
  tags?: string[];
  estimatedTime?: number;
}

export interface CodingAIChatMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: string;
  qualityScore?: {
    overall: number;
    clarity: number;
    context: number;
    specificity: number;
    feedback: string;
  };
}

export interface CodingExecutionResult {
  passed: boolean;
  passedCount: number;
  totalCount: number;
  testCases: CodingTestCase[];
  executionTimeMs: number;
  compileOutput?: string;
  runtimeOutput?: string;
}

export interface CodingAssessmentResult {
  questionId: string;
  questionTitle: string;
  difficulty: string;
  topic: string;
  language: string;
  testsPassed: number;
  totalTests: number;
  score: number;
  timeSpentSeconds: number;
  promptCount: number;
  avgPromptScore: number;
  breakdown: {
    codeCorrectness: number;
    timeEfficiency: number;
    aiLiteracyScore: number;
  };
}

