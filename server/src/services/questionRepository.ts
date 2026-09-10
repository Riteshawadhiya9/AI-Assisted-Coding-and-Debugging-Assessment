import fs from 'fs';
import path from 'path';
import { Question, SanitizedQuestion, QuestionFilters } from '../types';
import { QuestionValidator } from '../validators/questionValidator';

export class QuestionRepository {
  private questions: Question[] = [];

  constructor() {
    this.loadQuestions();
  }

  private getDbPath(): string {
    const candidatePaths = [
      path.join(__dirname, '..', 'data', 'questions.json'),
      path.join(__dirname, '..', '..', 'src', 'data', 'questions.json'),
      path.join(process.cwd(), 'src', 'data', 'questions.json'),
      path.join(process.cwd(), 'server', 'src', 'data', 'questions.json')
    ];
    for (const p of candidatePaths) {
      if (fs.existsSync(p)) {
        return p;
      }
    }
    return candidatePaths[0];
  }

  private loadQuestions(): void {
    try {
      const dbPath = this.getDbPath();
      if (fs.existsSync(dbPath)) {
        const fileContent = fs.readFileSync(dbPath, 'utf8');
        const parsed: any[] = JSON.parse(fileContent);

        // Validate entire question bank
        const validation = QuestionValidator.validateQuestionBank(parsed);
        if (!validation.isValid) {
          console.error('QuestionRepository: Data validation failed for question bank:');
          for (const [qId, errors] of Object.entries(validation.errorsByQuestion)) {
            console.error(`  - ${qId}: ${errors.join('; ')}`);
          }
        }

        this.questions = parsed as Question[];
        console.log(`QuestionRepository: Loaded and validated ${this.questions.length} questions successfully (${validation.validCount} valid).`);
      } else {
        console.warn(`QuestionRepository: Database not found at candidate paths. Using empty array.`);
        this.questions = [];
      }
    } catch (error) {
      console.error('QuestionRepository: Error loading questions database:', error);
      this.questions = [];
    }
  }

  /**
   * Sanitizes a question by omitting correctCode, bugList, primaryBugType, explanation, bugConcept,
   * and protecting hidden test cases so they cannot be inspected in the client before submission.
   */
  public sanitize(q: Question): SanitizedQuestion {
    const { correctCode, bugList, primaryBugType, explanation, bugConcept, hiddenTestCases, ...sanitized } = q;
    
    // Sanitize implementations by removing correctCode
    let sanitizedImplementations: any = undefined;
    if (q.implementations) {
      sanitizedImplementations = {
        c: { buggyCode: q.implementations.c?.buggyCode || '' },
        cpp: { buggyCode: q.implementations.cpp?.buggyCode || '' },
        java: { buggyCode: q.implementations.java?.buggyCode || '' }
      };
    }

    return {
      ...sanitized,
      implementations: sanitizedImplementations,
      hiddenTestCases: []
    };
  }

  public getById(id: string, sanitize?: true): SanitizedQuestion | undefined;
  public getById(id: string, sanitize: false): Question | undefined;
  public getById(id: string, sanitize = true): Question | SanitizedQuestion | undefined {
    const q = this.questions.find((x) => x.id === id);
    if (!q) return undefined;
    return sanitize ? this.sanitize(q) : q;
  }

  public getAll(sanitize?: true): SanitizedQuestion[];
  public getAll(sanitize: false): Question[];
  public getAll(sanitize = true): (Question | SanitizedQuestion)[] {
    return sanitize ? this.questions.map((q) => this.sanitize(q)) : this.questions;
  }

  public query(filters: QuestionFilters, sanitize?: true): SanitizedQuestion[];
  public query(filters: QuestionFilters, sanitize: false): Question[];
  public query(filters: QuestionFilters, sanitize = true): (Question | SanitizedQuestion)[] {
    let list = this.questions;

    if (filters.language) {
      const targetLang = filters.language.toLowerCase();
      list = list.filter((q) => {
        if (q.implementations && q.implementations[targetLang as keyof typeof q.implementations]) {
          return true;
        }
        return q.language?.toLowerCase() === targetLang;
      });
    }

    if (filters.difficulty) {
      list = list.filter((q) => q.difficulty.toLowerCase() === filters.difficulty!.toLowerCase());
    }

    if (filters.topic && filters.topic !== 'random') {
      const t = filters.topic;
      list = list.filter((q) => {
        if (t === 'trees') {
          return q.topic === 'trees' || q.subtopic?.includes('bst') || q.subtopic?.includes('tree');
        }
        if (t === 'graphs') {
          return q.topic === 'graphs' || q.subtopic?.includes('graph') || q.subtopic?.includes('bfs') || q.subtopic?.includes('dfs');
        }
        if (t === '2ddp') {
          return q.topic === '2ddp' || q.subtopic?.includes('dp') || q.subtopic?.includes('knapsack') || q.subtopic?.includes('lcs');
        }
        if (t === 'advanced-dsa') {
          return q.topic === 'advanced-dsa';
        }
        return q.topic === t;
      });
    }

    if (filters.search) {
      const qLower = filters.search.toLowerCase().trim();
      list = list.filter((q) =>
        q.title.toLowerCase().includes(qLower) ||
        q.subtopic.toLowerCase().includes(qLower) ||
        q.tags.some((tag) => tag.toLowerCase().includes(qLower))
      );
    }

    return sanitize ? list.map((q) => this.sanitize(q)) : list;
  }

  public filterByTopic(topic: string, sanitize?: true): SanitizedQuestion[];
  public filterByTopic(topic: string, sanitize: false): Question[];
  public filterByTopic(topic: string, sanitize = true): (Question | SanitizedQuestion)[] {
    const list = this.questions.filter((q) => q.topic === topic || topic === 'random');
    return sanitize ? list.map((q) => this.sanitize(q)) : list;
  }

  public filterByLanguage(language: string, sanitize?: true): SanitizedQuestion[];
  public filterByLanguage(language: string, sanitize: false): Question[];
  public filterByLanguage(language: string, sanitize = true): (Question | SanitizedQuestion)[] {
    const targetLang = language.toLowerCase();
    const list = this.questions.filter((q) => {
      if (q.implementations && q.implementations[targetLang as keyof typeof q.implementations]) {
        return true;
      }
      return q.language?.toLowerCase() === targetLang;
    });
    return sanitize ? list.map((q) => this.sanitize(q)) : list;
  }

  public filterByDifficulty(difficulty: string, sanitize?: true): SanitizedQuestion[];
  public filterByDifficulty(difficulty: string, sanitize: false): Question[];
  public filterByDifficulty(difficulty: string, sanitize = true): (Question | SanitizedQuestion)[] {
    const list = this.questions.filter((q) => q.difficulty.toLowerCase() === difficulty.toLowerCase());
    return sanitize ? list.map((q) => this.sanitize(q)) : list;
  }

  public getRandom(filters: QuestionFilters, sanitize?: true): SanitizedQuestion | undefined;
  public getRandom(filters: QuestionFilters, sanitize: false): Question | undefined;
  public getRandom(
    filters: QuestionFilters,
    sanitize = true
  ): Question | SanitizedQuestion | undefined {
    const list = this.query(filters, false);

    if (list.length === 0) return undefined;
    const randomIndex = Math.floor(Math.random() * list.length);
    const selected = list[randomIndex];
    return sanitize ? this.sanitize(selected) : selected;
  }
}

export const questionRepository = new QuestionRepository();
export default questionRepository;

