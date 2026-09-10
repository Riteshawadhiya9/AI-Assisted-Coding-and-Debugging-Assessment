import { Question, Language, Difficulty, BugType } from '../types';

export interface ValidationResult {
  valid: boolean;
  errors: string[];
}

export interface BankValidationResult {
  total: number;
  validCount: number;
  invalidCount: number;
  errorsByQuestion: Record<string, string[]>;
  isValid: boolean;
}

const VALID_LANGUAGES: Language[] = ['c', 'cpp', 'java'];
const VALID_DIFFICULTIES: Difficulty[] = ['easy', 'medium', 'hard'];
const VALID_BUG_TYPES: BugType[] = [
  'syntax',
  'compilation',
  'runtime',
  'logical',
  'boundary',
  'off-by-one',
  'incorrect condition',
  'incorrect initialization',
  'incorrect recursion',
  'incorrect traversal',
  'incorrect state transition',
  'incorrect data structure usage',
  'time complexity',
  'integer overflow',
  'edge case'
];

export class QuestionValidator {
  public static validateQuestion(q: any): ValidationResult {
    const errors: string[] = [];

    if (!q || typeof q !== 'object') {
      return { valid: false, errors: ['Question must be a valid object'] };
    }

    // Required string properties
    const stringFields = ['id', 'title', 'problemStatement', 'subtopic', 'explanation', 'intendedApproach'];
    for (const field of stringFields) {
      if (!q[field] || typeof q[field] !== 'string' || q[field].trim() === '') {
        errors.push(`Field '${field}' is required and must be a non-empty string`);
      }
    }

    // Multi-language Implementations check
    if (q.implementations && typeof q.implementations === 'object') {
      for (const lang of VALID_LANGUAGES) {
        const impl = q.implementations[lang];
        if (!impl || typeof impl !== 'object') {
          errors.push(`implementations.${lang} must be an object`);
        } else {
          if (!impl.buggyCode || typeof impl.buggyCode !== 'string' || impl.buggyCode.trim() === '') {
            errors.push(`implementations.${lang}.buggyCode is required and must be non-empty`);
          } else {
            // Buggy code must look like realistic interview/production code without clues or bug-revealing comments
            const bannedPattern = /\/\/\s*(BUG|incorrect|fix|wrong|intentional|this causes|TODO)|\/\*[\s\S]*?(BUG|incorrect|fix|wrong|intentional|this causes|TODO)[\s\S]*?\*\//i;
            if (bannedPattern.test(impl.buggyCode)) {
              errors.push(`implementations.${lang}.buggyCode must not contain bug-revealing comments`);
            }
          }
          if (!impl.correctCode || typeof impl.correctCode !== 'string' || impl.correctCode.trim() === '') {
            errors.push(`implementations.${lang}.correctCode is required and must be non-empty`);
          }
        }
      }
    } else {
      // Legacy fallback
      if (!q.buggyCode || typeof q.buggyCode !== 'string' || q.buggyCode.trim() === '') {
        errors.push(`Field 'buggyCode' or 'implementations' is required`);
      } else {
        const bannedPattern = /\/\/\s*(BUG|incorrect|fix|wrong|intentional|this causes|TODO)|\/\*[\s\S]*?(BUG|incorrect|fix|wrong|intentional|this causes|TODO)[\s\S]*?\*\//i;
        if (bannedPattern.test(q.buggyCode)) {
          errors.push(`Field 'buggyCode' must not contain bug-revealing comments`);
        }
      }
      if (!q.correctCode || typeof q.correctCode !== 'string' || q.correctCode.trim() === '') {
        errors.push(`Field 'correctCode' or 'implementations' is required`);
      }
    }

    // Difficulty check
    if (!VALID_DIFFICULTIES.includes(q.difficulty)) {
      errors.push(`Invalid difficulty '${q.difficulty}'. Must be one of: ${VALID_DIFFICULTIES.join(', ')}`);
    }

    // Estimated time check
    if (typeof q.estimatedTime !== 'number' || q.estimatedTime <= 0) {
      errors.push(`Field 'estimatedTime' must be a positive number (estimated minutes)`);
    }

    // Primary bug type check
    if (!VALID_BUG_TYPES.includes(q.primaryBugType)) {
      errors.push(`Invalid primaryBugType '${q.primaryBugType}'. Must be one of: ${VALID_BUG_TYPES.join(', ')}`);
    }

    // Constraints check
    if (!Array.isArray(q.constraints) || q.constraints.length === 0) {
      errors.push(`Field 'constraints' must be a non-empty array of strings`);
    }

    // Visible Test Cases check
    if (!Array.isArray(q.visibleTestCases) || q.visibleTestCases.length === 0) {
      errors.push(`Field 'visibleTestCases' must be a non-empty array with at least 1 test case`);
    } else {
      q.visibleTestCases.forEach((tc: any, idx: number) => {
        if (typeof tc.id !== 'number') errors.push(`visibleTestCases[${idx}].id must be a number`);
        if (typeof tc.input !== 'string') errors.push(`visibleTestCases[${idx}].input must be a string`);
        if (typeof tc.expectedOutput !== 'string') errors.push(`visibleTestCases[${idx}].expectedOutput must be a string`);
        if (tc.isHidden !== false) errors.push(`visibleTestCases[${idx}].isHidden must be false`);
      });
    }

    // Hidden Test Cases check
    if (!Array.isArray(q.hiddenTestCases) || q.hiddenTestCases.length === 0) {
      errors.push(`Field 'hiddenTestCases' must be a non-empty array with at least 1 test case`);
    } else {
      q.hiddenTestCases.forEach((tc: any, idx: number) => {
        if (typeof tc.id !== 'number') errors.push(`hiddenTestCases[${idx}].id must be a number`);
        if (typeof tc.input !== 'string') errors.push(`hiddenTestCases[${idx}].input must be a string`);
        if (typeof tc.expectedOutput !== 'string') errors.push(`hiddenTestCases[${idx}].expectedOutput must be a string`);
        if (tc.isHidden !== true) errors.push(`hiddenTestCases[${idx}].isHidden must be true`);
      });
    }

    // Expected Complexity check
    if (!q.expectedComplexity || typeof q.expectedComplexity !== 'object') {
      errors.push(`Field 'expectedComplexity' must be an object with 'time' and 'space' strings`);
    } else {
      if (!q.expectedComplexity.time || typeof q.expectedComplexity.time !== 'string') {
        errors.push(`expectedComplexity.time must be a non-empty string`);
      }
      if (!q.expectedComplexity.space || typeof q.expectedComplexity.space !== 'string') {
        errors.push(`expectedComplexity.space must be a non-empty string`);
      }
    }

    // Tags check
    if (!Array.isArray(q.tags) || q.tags.length === 0) {
      errors.push(`Field 'tags' must be a non-empty array of strings`);
    }

    return {
      valid: errors.length === 0,
      errors
    };
  }

  public static validateQuestionBank(questions: any[]): BankValidationResult {
    const errorsByQuestion: Record<string, string[]> = {};
    const seenIds = new Set<string>();
    const seenTitles = new Set<string>();
    let validCount = 0;
    let invalidCount = 0;

    for (let i = 0; i < questions.length; i++) {
      const q = questions[i];
      const qId = q?.id || `index_${i}`;
      const res = this.validateQuestion(q);

      if (q?.id) {
        if (seenIds.has(q.id)) {
          res.valid = false;
          res.errors.push(`Duplicate question id: ${q.id}`);
        }
        seenIds.add(q.id);
      }

      if (q?.title) {
        if (seenTitles.has(q.title)) {
          res.valid = false;
          res.errors.push(`Duplicate question title: ${q.title}`);
        }
        seenTitles.add(q.title);
      }

      if (res.valid) {
        validCount++;
      } else {
        invalidCount++;
        errorsByQuestion[qId] = res.errors;
      }
    }

    return {
      total: questions.length,
      validCount,
      invalidCount,
      errorsByQuestion,
      isValid: invalidCount === 0
    };
  }
}

