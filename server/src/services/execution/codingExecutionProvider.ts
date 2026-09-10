/**
 * ============================================================================
 * MOCK CODING EXECUTION PROVIDER
 * ============================================================================
 * Deterministic mock execution provider for coding questions.
 * Compares user code against solution code (normalized) to determine
 * pass/fail for test cases.
 *
 * Implements the same IExecutionProvider interface so it can be replaced
 * with Judge0 later.
 * ============================================================================
 */

import { codingQuestionRepository } from '../codingQuestionRepository';
import { CodingLanguage } from '../../types/codingTypes';

export interface CodingTestResult {
  testCaseId: number;
  passed: boolean;
  input: string;
  expectedOutput: string;
  actualOutput: string;
  isHidden: boolean;
}

export interface CodingExecutionResult {
  passed: boolean;
  compileOutput: string;
  runtimeOutput: string;
  executionTimeMs: number;
  memoryUsedKb: number;
  testResults: CodingTestResult[];
  passedCount: number;
  totalCount: number;
}

export class CodingExecutionProvider {
  /**
   * Normalize code for deterministic comparison:
   * strip comments, normalize whitespace.
   */
  private normalizeCode(source: string): string {
    if (!source) return '';
    const noComments = source
      .replace(/\/\*[\s\S]*?\*\//g, '')            // block comments
      .replace(/([^\\:]|^)\/\/.*$/gm, '$1')         // line comments (JS/C/Java)
      .replace(/#.*$/gm, '');                        // Python comments
    return noComments.replace(/\s+/g, ' ').trim();
  }

  public async execute(
    code: string,
    questionId: string,
    language: CodingLanguage = 'python',
    isSubmission = false
  ): Promise<CodingExecutionResult> {
    const question = codingQuestionRepository.getById(questionId, false);
    if (!question) {
      throw new Error(`Coding question '${questionId}' not found.`);
    }

    const userNormalized = this.normalizeCode(code);
    const solutionCode = question.solutionCode?.[language] || '';
    const solutionNormalized = this.normalizeCode(solutionCode);
    const starterCode = question.starterCode?.[language] || '';
    const starterNormalized = this.normalizeCode(starterCode);

    // Determine if user's code matches solution
    const isCorrect = solutionNormalized.length > 0 && userNormalized === solutionNormalized;
    const isStillStarter = userNormalized === starterNormalized;

    // If user hasn't changed the starter code, partial fail
    // If user wrote something but doesn't match solution, partial pass (some tests pass)
    const hasAttempted = !isStillStarter && userNormalized.length > starterNormalized.length * 0.5;

    const testResults: CodingTestResult[] = [];

    for (const tc of question.testCases) {
      if (isCorrect) {
        testResults.push({
          testCaseId: tc.id,
          passed: true,
          input: tc.input,
          expectedOutput: tc.isHidden && !isSubmission ? '[Hidden]' : tc.expectedOutput,
          actualOutput: tc.expectedOutput,
          isHidden: tc.isHidden,
        });
      } else if (hasAttempted) {
        // Simulate partial correctness — some visible tests might pass
        const passChance = tc.isHidden ? 0.3 : 0.5;
        const passed = Math.random() < passChance;
        testResults.push({
          testCaseId: tc.id,
          passed,
          input: tc.input,
          expectedOutput: tc.isHidden && !isSubmission ? '[Hidden]' : tc.expectedOutput,
          actualOutput: passed
            ? tc.expectedOutput
            : `Incorrect output for input: ${tc.input}`,
          isHidden: tc.isHidden,
        });
      } else {
        testResults.push({
          testCaseId: tc.id,
          passed: false,
          input: tc.input,
          expectedOutput: tc.isHidden && !isSubmission ? '[Hidden]' : tc.expectedOutput,
          actualOutput: isStillStarter
            ? 'No output — starter code has not been modified.'
            : 'Incorrect output.',
          isHidden: tc.isHidden,
        });
      }
    }

    const passedCount = testResults.filter(r => r.passed).length;
    const totalCount = testResults.length;
    const allPassed = passedCount === totalCount;

    const compileOutput = isStillStarter
      ? `[Mock Compiler] ${language.toUpperCase()}: Compiled. Warning: code appears to be unmodified starter code.`
      : `[Mock Compiler] ${language.toUpperCase()}: Build succeeded.`;

    const runtimeOutput = isStillStarter
      ? `[Mock Runner] Starter code executed. No meaningful output.`
      : allPassed
        ? `[Mock Runner] All ${totalCount} tests passed in ${(Math.random() * 0.05 + 0.01).toFixed(3)}s.`
        : `[Mock Runner] ${passedCount}/${totalCount} tests passed.`;

    return {
      passed: allPassed,
      compileOutput,
      runtimeOutput,
      executionTimeMs: Math.floor(Math.random() * 20) + 10,
      memoryUsedKb: Math.floor(Math.random() * 1024) + 2048,
      testResults,
      passedCount,
      totalCount,
    };
  }
}

export const codingExecutionProvider = new CodingExecutionProvider();
