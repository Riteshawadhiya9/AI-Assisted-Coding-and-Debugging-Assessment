import { questionRepository } from '../questionRepository';
import { IExecutionProvider, ExecutionResult, ExecutionOptions, TestCaseExecutionResult } from './executionProvider';
import { Question } from '../../types';

/**
 * ============================================================================
 * MOCK EXECUTION PROVIDER (PHASE 4)
 * ============================================================================
 * NOTICE: This is a deterministic local mock execution provider.
 * It simulates compilation and test case execution by evaluating algorithmic
 * solutions against the repository's ground truth (correctCode and buggyCode).
 *
 * It demonstrates:
 * - Run Code & test case execution
 * - Passed/Failed tests with expected vs actual output
 * - Compiler and runtime diagnostic outputs
 * - Submission evaluation including bug diagnosis verification
 *
 * This provider implements `IExecutionProvider` so it can later be seamlessly
 * replaced with `Judge0ExecutionProvider` or a sandboxed runner in future phases
 * without requiring changes to the frontend or API layer.
 * ============================================================================
 */
export class MockExecutionProvider implements IExecutionProvider {
  /**
   * Normalizes code for deterministic evaluation by stripping comments,
   * leading/trailing whitespace, and redundant newlines.
   */
  private normalizeCode(source: string): string {
    if (!source) return '';
    // Strip multi-line comments /* ... */ and single-line comments // ...
    const noComments = source.replace(/\/\*[\s\S]*?\*\/|([^\\:]|^)\/\/.*$/gm, '$1');
    // Normalize all whitespace sequences to a single space and trim
    return noComments.replace(/\s+/g, ' ').trim();
  }

  public async execute(
    code: string,
    questionId: string,
    options: ExecutionOptions = {}
  ): Promise<ExecutionResult> {
    const question = questionRepository.getById(questionId, false) as Question | undefined;
    if (!question) {
      throw new Error(`Question with ID '${questionId}' was not found in the repository.`);
    }

    const userNormalized = this.normalizeCode(code);
    const lang = options.language || question.language || 'cpp';

    let correctCode = question.correctCode;
    let buggyCode = question.buggyCode;

    if (question.implementations && question.implementations[lang]) {
      correctCode = question.implementations[lang].correctCode;
      buggyCode = question.implementations[lang].buggyCode;
    }

    const correctNormalized = this.normalizeCode(correctCode || '');
    const buggyNormalized = this.normalizeCode(buggyCode || '');

    // Determine if user's code matches the correct solution
    const isFixed = userNormalized === correctNormalized;
    const isStillOriginalBuggy = userNormalized === buggyNormalized;

    const testResults: TestCaseExecutionResult[] = [];

    // 1. Evaluate Visible Test Cases
    for (const tc of question.visibleTestCases) {
      if (isFixed) {
        testResults.push({
          testCaseId: tc.id,
          passed: true,
          actualOutput: tc.expectedOutput,
          expectedOutput: tc.expectedOutput,
          isHidden: false
        });
      } else {
        const failureReason = isStillOriginalBuggy
          ? `Mismatch: Expected '${tc.expectedOutput}', but algorithm produced incorrect state due to '${question.primaryBugType}'.`
          : `Mismatch: Expected '${tc.expectedOutput}', but got unexpected test result.`;
        
        testResults.push({
          testCaseId: tc.id,
          passed: false,
          actualOutput: failureReason,
          expectedOutput: tc.expectedOutput,
          isHidden: false
        });
      }
    }

    // 2. Evaluate Hidden Test Cases
    for (const tc of question.hiddenTestCases) {
      if (isFixed) {
        testResults.push({
          testCaseId: tc.id,
          passed: true,
          actualOutput: options.isSubmission ? tc.expectedOutput : '[Hidden Test Output - Passed]',
          expectedOutput: options.isSubmission ? tc.expectedOutput : undefined,
          isHidden: true
        });
      } else {
        testResults.push({
          testCaseId: tc.id,
          passed: false,
          actualOutput: options.isSubmission ? `Mismatch on hidden test case (Expected: ${tc.expectedOutput})` : '[Hidden Test Output - Failed]',
          expectedOutput: options.isSubmission ? tc.expectedOutput : undefined,
          isHidden: true
        });
      }
    }

    const allPassed = testResults.every((r) => r.passed);
    const visiblePassed = testResults.filter((r) => !r.isHidden && r.passed).length;
    const totalVisible = question.visibleTestCases.length;

    // Check user diagnosis if provided
    let diagnosisCorrect: boolean | undefined = undefined;
    if (options.userDiagnosis && options.userDiagnosis.bugType) {
      diagnosisCorrect = options.userDiagnosis.bugType.toLowerCase() === question.primaryBugType.toLowerCase();
    }

    // Realistic mock compiler and runtime messages
    const compileOutput = isFixed
      ? `[Local Mock Compiler] Target: ${lang.toUpperCase()}\n[Local Mock Compiler] Status: Build succeeded (0 errors, 0 warnings).`
      : `[Local Mock Compiler] Target: ${lang.toUpperCase()}\n[Local Mock Compiler] Status: Compiled with warnings. Logical bug suspected.`;

    const runtimeOutput = isFixed
      ? `[Local Mock Runner] Executed ${testResults.length} test assertions.\n[Local Mock Runner] All test cases passed in ${(Math.random() * 0.05 + 0.01).toFixed(3)}s.`
      : `[Local Mock Runner] Executed ${testResults.length} test assertions.\n[Local Mock Runner] ${visiblePassed}/${totalVisible} visible test cases passed. Assertion failure detected on test input.`;

    return {
      passed: allPassed,
      compileOutput,
      runtimeOutput,
      executionTimeMs: Math.floor(Math.random() * 15) + 12,
      memoryUsedKb: Math.floor(Math.random() * 1024) + 2048,
      testResults,
      diagnosisCorrect,
      actualBugType: options.isSubmission ? question.primaryBugType : undefined
    };
  }
}

export const mockExecutionProvider = new MockExecutionProvider();
export default mockExecutionProvider;
