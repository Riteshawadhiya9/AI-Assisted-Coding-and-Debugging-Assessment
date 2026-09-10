/**
 * ============================================================================
 * CODING ROUTES — AI-ASSISTED CODING SECTION
 * ============================================================================
 * Express routes under /api/coding/ for the coding assessment section.
 * ============================================================================
 */

import { Router, Request, Response } from 'express';
import { codingQuestionRepository } from '../services/codingQuestionRepository';
import { codingAIService, CodingAIQuery } from '../services/ai/codingAIService';
import { codingExecutionProvider } from '../services/execution/codingExecutionProvider';
import { CodingLanguage } from '../types/codingTypes';

const router = Router();

// ─── Question Endpoints ──────────────────────────────────────────────────────

// GET /api/coding/questions — List all coding questions (filtered, sanitized)
router.get('/questions', (req: Request, res: Response) => {
  try {
    const { topic, difficulty, search } = req.query;
    const filters = {
      topic: topic as string | undefined,
      difficulty: difficulty as string | undefined,
      search: search as string | undefined,
    };

    const hasFilters = topic || difficulty || search;
    const questions = hasFilters
      ? codingQuestionRepository.query(filters, true)
      : codingQuestionRepository.getAll(true);

    res.json(questions);
  } catch (error) {
    console.error('codingRoutes GET /questions error:', error);
    res.status(500).json({ error: 'Failed to retrieve coding questions' });
  }
});

// GET /api/coding/questions/topics — Get all available topics
router.get('/questions/topics', (_req: Request, res: Response) => {
  try {
    const topics = codingQuestionRepository.getTopics();
    res.json(topics);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve topics' });
  }
});

// GET /api/coding/questions/stats — Get question bank statistics
router.get('/questions/stats', (_req: Request, res: Response) => {
  try {
    const stats = codingQuestionRepository.getStats();
    res.json(stats);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve stats' });
  }
});

// GET /api/coding/questions/random — Random coding question
router.get('/questions/random', (req: Request, res: Response) => {
  try {
    const { topic, difficulty } = req.query;
    const question = codingQuestionRepository.getRandom(
      {
        topic: topic as string | undefined,
        difficulty: difficulty as string | undefined,
      },
      true
    );

    if (!question) {
      return res.status(404).json({ error: 'No coding question matches the specified criteria' });
    }
    res.json(question);
  } catch (error) {
    console.error('codingRoutes GET /questions/random error:', error);
    res.status(500).json({ error: 'Failed to retrieve random coding question' });
  }
});

// GET /api/coding/questions/:id — Single coding question by ID
router.get('/questions/:id', (req: Request, res: Response) => {
  try {
    const question = codingQuestionRepository.getById(req.params.id, true);
    if (!question) {
      return res.status(404).json({ error: 'Coding question not found' });
    }
    res.json(question);
  } catch (error) {
    console.error('codingRoutes GET /questions/:id error:', error);
    res.status(500).json({ error: 'Failed to retrieve coding question' });
  }
});

// GET /api/coding/questions/:id/solution — Full question with solution (post-submission)
router.get('/questions/:id/solution', (req: Request, res: Response) => {
  try {
    const question = codingQuestionRepository.getById(req.params.id, false);
    if (!question) {
      return res.status(404).json({ error: 'Coding question not found' });
    }
    res.json(question);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve solution' });
  }
});

// ─── Execution Endpoint ──────────────────────────────────────────────────────

// POST /api/coding/execute — Execute code against test cases
router.post('/execute', async (req: Request, res: Response) => {
  try {
    const { code, questionId, language, isSubmission } = req.body;

    if (!code || typeof code !== 'string') {
      return res.status(400).json({ error: 'Missing or invalid code' });
    }
    if (!questionId || typeof questionId !== 'string') {
      return res.status(400).json({ error: 'Missing questionId' });
    }

    const result = await codingExecutionProvider.execute(
      code,
      questionId,
      (language as CodingLanguage) || 'python',
      Boolean(isSubmission)
    );

    res.json(result);
  } catch (error: any) {
    console.error('codingRoutes POST /execute error:', error);
    res.status(500).json({ error: error.message || 'Execution failed' });
  }
});

// ─── AI Endpoints ────────────────────────────────────────────────────────────

// GET /api/coding/ai/status — AI provider status
router.get('/ai/status', (_req: Request, res: Response) => {
  const status = codingAIService.getStatus();
  res.json(status);
});

// POST /api/coding/ai/chat — AI assistant chat
router.post('/ai/chat', async (req: Request, res: Response) => {
  try {
    const {
      questionId,
      message,
      prompt,
      currentEditorCode,
      currentCode,
      userCode,
      selectedLanguage,
      language,
      latestRunResult,
      mode,
      history,
      conversationHistory,
      action,
      currentSessionTokens,
      tokensUsed,
      conversationTokensUsed,
    } = req.body;

    const actualMessage = message || prompt;
    if (!questionId || typeof questionId !== 'string') {
      return res.status(400).json({ error: 'questionId is required' });
    }
    if (!actualMessage || typeof actualMessage !== 'string') {
      return res.status(400).json({ error: 'message or prompt is required' });
    }

    const sessionTokens = Number(currentSessionTokens ?? tokensUsed ?? conversationTokensUsed ?? 0);

    const query: CodingAIQuery = {
      questionId,
      message: actualMessage,
      currentEditorCode: currentEditorCode || currentCode || userCode,
      selectedLanguage: selectedLanguage || language || 'python',
      latestRunResult,
      mode: mode || 'practice',
      history: history || conversationHistory,
      action: action || 'chat',
      currentSessionTokens: isNaN(sessionTokens) ? 0 : sessionTokens,
    };

    const response = await codingAIService.handleChat(query);
    res.json({
      ...response,
      reply: response.message,
      message: response.message,
      tokensUsed: response.tokensUsed,
      tokensRemaining: response.tokensRemaining,
      tokenLimitReached: response.tokenLimitReached,
      tokensThisTurn: response.tokensThisTurn,
      isExact: response.isExact,
      estimationMethod: response.estimationMethod,
    });
  } catch (error: any) {
    console.error('codingRoutes POST /ai/chat error:', error);
    res.status(500).json({
      message: 'AI assistant unavailable. Please try again.',
      type: 'error-help',
      revealsSolution: false,
      providerUsed: 'fallback-error',
    });
  }
});

// POST /api/coding/ai/improve-prompt — "Improve My Prompt" action
router.post('/ai/improve-prompt', async (req: Request, res: Response) => {
  try {
    const { questionId, message, selectedLanguage, mode } = req.body;

    if (!questionId) {
      return res.status(400).json({ error: 'questionId is required' });
    }
    if (!message) {
      return res.status(400).json({ error: 'message (the prompt to improve) is required' });
    }

    const query: CodingAIQuery = {
      questionId,
      message,
      selectedLanguage: selectedLanguage || 'python',
      mode: mode || 'practice',
      action: 'improve-prompt',
    };

    const response = await codingAIService.handleChat(query);
    res.json(response);
  } catch (error: any) {
    console.error('codingRoutes POST /ai/improve-prompt error:', error);
    res.status(500).json({ error: 'Prompt improvement service unavailable' });
  }
});

export default router;
