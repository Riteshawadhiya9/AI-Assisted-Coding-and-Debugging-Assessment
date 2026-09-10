/**
 * ============================================================================
 * CODING QUESTION REPOSITORY
 * ============================================================================
 * Provides query, filter, and random-access operations over the coding
 * question bank.  Mirrors the pattern used by questionRepository.ts for the
 * debugging section.
 * ============================================================================
 */

import codingQuestions from '../data/codingQuestions';
import { CodingQuestion } from '../types/codingTypes';

export interface CodingQueryFilters {
  topic?: string;
  difficulty?: string;
  language?: string;
  search?: string;
}

export class CodingQuestionRepository {
  private questions: CodingQuestion[];

  constructor() {
    this.questions = codingQuestions;
    console.log(`[CodingQuestionRepository] Loaded ${this.questions.length} coding questions.`);
  }

  /** Sanitize a question for client consumption (strip solution code). */
  private sanitize(q: CodingQuestion): Omit<CodingQuestion, 'solutionCode'> & { solutionCode?: undefined } {
    const { solutionCode, ...rest } = q;
    // Also hide hidden test expected outputs
    const sanitizedTests = rest.testCases.map(tc => ({
      ...tc,
      expectedOutput: tc.isHidden ? '[Hidden]' : tc.expectedOutput,
    }));
    return { ...rest, testCases: sanitizedTests };
  }

  /** Get all questions, optionally sanitized. */
  public getAll(sanitized = true): CodingQuestion[] {
    if (sanitized) {
      return this.questions.map(q => this.sanitize(q) as CodingQuestion);
    }
    return [...this.questions];
  }

  /** Get a question by ID. */
  public getById(id: string, sanitized = true): CodingQuestion | undefined {
    const q = this.questions.find(q => q.id === id);
    if (!q) return undefined;
    return sanitized ? (this.sanitize(q) as CodingQuestion) : q;
  }

  /** Query questions with optional filters. */
  public query(filters: CodingQueryFilters, sanitized = true): CodingQuestion[] {
    let results = [...this.questions];

    if (filters.topic) {
      const topic = filters.topic.toLowerCase();
      results = results.filter(q =>
        q.topic.toLowerCase() === topic ||
        q.tags.some(t => t.toLowerCase() === topic)
      );
    }

    if (filters.difficulty) {
      const diff = filters.difficulty.toLowerCase();
      results = results.filter(q => q.difficulty === diff);
    }

    if (filters.search) {
      const search = filters.search.toLowerCase();
      results = results.filter(q =>
        q.title.toLowerCase().includes(search) ||
        q.topic.toLowerCase().includes(search) ||
        q.tags.some(t => t.toLowerCase().includes(search))
      );
    }

    if (sanitized) {
      return results.map(q => this.sanitize(q) as CodingQuestion);
    }
    return results;
  }

  /** Get a random question matching optional filters. */
  public getRandom(filters: CodingQueryFilters = {}, sanitized = true): CodingQuestion | undefined {
    const candidates = this.query(filters, false);
    if (candidates.length === 0) return undefined;
    const idx = Math.floor(Math.random() * candidates.length);
    const q = candidates[idx];
    return sanitized ? (this.sanitize(q) as CodingQuestion) : q;
  }

  /** Get all unique topics. */
  public getTopics(): string[] {
    const topicSet = new Set<string>();
    for (const q of this.questions) {
      topicSet.add(q.topic);
    }
    return Array.from(topicSet).sort();
  }

  /** Get statistics. */
  public getStats(): { total: number; byDifficulty: Record<string, number>; byTopic: Record<string, number> } {
    const byDifficulty: Record<string, number> = {};
    const byTopic: Record<string, number> = {};
    for (const q of this.questions) {
      byDifficulty[q.difficulty] = (byDifficulty[q.difficulty] || 0) + 1;
      byTopic[q.topic] = (byTopic[q.topic] || 0) + 1;
    }
    return { total: this.questions.length, byDifficulty, byTopic };
  }
}

export const codingQuestionRepository = new CodingQuestionRepository();
