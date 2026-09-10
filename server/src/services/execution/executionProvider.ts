export interface TestCaseExecutionResult {
  testCaseId: number;
  passed: boolean;
  actualOutput: string;
  expectedOutput?: string;
  isHidden: boolean;
}

export interface ExecutionResult {
  passed: boolean;
  compileOutput?: string;
  runtimeOutput?: string;
  executionTimeMs?: number;
  memoryUsedKb?: number;
  testResults: TestCaseExecutionResult[];
  diagnosisCorrect?: boolean;
  actualBugType?: string;
}

import { Language } from '../../types';

export interface ExecutionOptions {
  language?: Language;
  isSubmission?: boolean;
  userDiagnosis?: {
    bugType?: string;
    notes?: string;
  };
}


export interface IExecutionProvider {
  /**
   * Executes source code against a given question's test cases.
   * In Phase 4, this is implemented deterministically by MockExecutionProvider.
   * In future phases, this can be swapped with Judge0ExecutionProvider without changing callers.
   */
  execute(code: string, questionId: string, options?: ExecutionOptions): Promise<ExecutionResult>;
}
