/**
 * ============================================================================
 * CODING QUESTION TYPES (AI-ASSISTED CODING SECTION)
 * ============================================================================
 * Shared type definitions for the AI-Assisted Coding assessment section.
 * These are distinct from the debugging question types.
 * ============================================================================
 */

export type CodingLanguage = 'c' | 'cpp' | 'java' | 'python' | 'javascript';

export interface CodingExample {
  input: string;
  output: string;
  explanation: string;
}

export interface CodingTestCase {
  id: number;
  input: string;
  expectedOutput: string;
  isHidden: boolean;
}

export interface CodingQuestion {
  id: string;
  title: string;
  difficulty: 'easy' | 'medium' | 'hard';
  topic: string;
  problemStatement: string;
  examples: CodingExample[];
  constraints: string[];
  functionSignature: Partial<Record<CodingLanguage, string>>;
  starterCode: Partial<Record<CodingLanguage, string>>;
  solutionCode?: Partial<Record<CodingLanguage, string>>;
  testCases: CodingTestCase[];
  tags: string[];
  estimatedTime: number; // minutes
}

export interface PromptQualityResult {
  score: number;           // 1-10
  strengths: string[];
  weaknesses: string[];
  improvedPrompt: string;
}

export interface CodingSessionPrompt {
  text: string;
  quality: number;
  timestamp: string;
}

export interface CodingSessionRunResult {
  passed: number;
  total: number;
  timestamp: string;
}

export interface CodingSession {
  id: string;
  problemId: string;
  language: CodingLanguage;
  mode: 'practice' | 'assessment';
  prompts: CodingSessionPrompt[];
  aiInteractions: number;
  codeChanges: number;
  runResults: CodingSessionRunResult[];
  finalCode: string;
  finalScore: number;
  timeStarted: string;
  timeCompleted?: string;
}

export interface CodingAssessmentResult {
  codingCorrectness: number;
  promptQuality: number;
  aiLiteracy: number;
  problemSolving: number;
  reviewAdaptation: number;
  overallScore: number;
  strengths: string[];
  weaknesses: string[];
  recommendations: string[];
}
