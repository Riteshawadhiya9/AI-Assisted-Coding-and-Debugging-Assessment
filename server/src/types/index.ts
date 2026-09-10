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
  correctCode: string;
}

export interface SanitizedLanguageImplementation {
  buggyCode: string;
}

export interface Question {
  id: string;
  title: string;
  problemStatement: string;
  topic: Topic;
  subtopic: string;
  difficulty: Difficulty;
  estimatedTime: number; // in minutes
  bugType?: BugType;
  primaryBugType: BugType;
  bugConcept: string;
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
  // Convenience & backward compatibility fields
  language?: Language;
  buggyCode?: string;
  correctCode?: string;
  bugList?: Bug[];
  explanation?: string;
}

export interface SanitizedQuestion {
  id: string;
  title: string;
  problemStatement: string;
  topic: Topic;
  subtopic: string;
  difficulty: Difficulty;
  estimatedTime: number;
  intendedApproach: string;
  constraints: string[];
  visibleTestCases: TestCase[];
  hiddenTestCases: TestCase[]; // Always empty before submission
  expectedComplexity: {
    time: string;
    space: string;
  };
  tags: string[];
  visualData?: VisualData;
  implementations: {
    c: SanitizedLanguageImplementation;
    cpp: SanitizedLanguageImplementation;
    java: SanitizedLanguageImplementation;
  };
  language?: Language;
  buggyCode?: string;
}

export interface QuestionFilters {
  language?: Language;
  topic?: Topic | string;
  difficulty?: Difficulty;
  search?: string;
}

export interface UserDiagnosis {
  bugType: BugType | '';
  notes: string;
  isLocked: boolean;
}

export interface ScoreBreakdown {
  correctness: number;
  tests: number;
  diagnosis: number;
  timeBonus: number;
  hintsPenalty: number;
  finalScore: number;
}
