import { Router, Request, Response } from 'express';
import { AIService, UserAIQuery } from '../services/ai/aiService';

const router = Router();
const aiService = new AIService();

// GET /api/ai/status - Returns configured provider status and fallback order (no secrets)
router.get('/status', (_req: Request, res: Response) => {
  const status = aiService.getStatus();
  res.json(status);
});

// POST /api/ai/chat - General conversation / prompt handler
router.post('/chat', async (req: Request, res: Response) => {
  try {
    const { 
      questionId, 
      message, 
      currentEditorCode,
      originalBuggyCode,
      lastRunCode,
      codeChangesDiff,
      latestExecutionResult,
      userCode, 
      executionOutput, 
      language, 
      mode, 
      isSubmitted, 
      history,
      type 
    } = req.body;

    if (!questionId || typeof questionId !== 'string') {
      return res.status(400).json({ error: 'questionId is required' });
    }

    if (!message || typeof message !== 'string') {
      return res.status(400).json({ error: 'message is required' });
    }

    const query: UserAIQuery = {
      questionId,
      message,
      currentEditorCode: currentEditorCode || userCode,
      originalBuggyCode,
      lastRunCode,
      codeChangesDiff,
      latestExecutionResult,
      userCode: currentEditorCode || userCode,
      executionOutput,
      language: language || 'cpp',
      mode: mode || 'practice',
      isSubmitted: Boolean(isSubmitted),
      type,
      history
    };

    const response = await aiService.handleChat(query);
    res.json(response);
  } catch (error: any) {
    console.error('aiRoutes /chat error:', error);
    res.status(500).json({
      message: 'Failed to process AI debugging query. Falling back to local assistance.',
      type: 'error-help',
      revealsSolution: false,
      providerUsed: 'fallback-error'
    });
  }
});

// POST /api/ai/hint - Quick Action: Give hint
router.post('/hint', async (req: Request, res: Response) => {
  try {
    const { questionId, userCode, executionOutput, language, mode, isSubmitted } = req.body;
    if (!questionId) return res.status(400).json({ error: 'questionId is required' });

    const promptMessage = mode === 'exam'
      ? 'Please give me a high-level conceptual hint or invariant to check for this problem.'
      : 'Give me a constructive debugging hint for my current approach.';

    const response = await aiService.handleChat({
      questionId,
      message: promptMessage,
      userCode,
      executionOutput,
      language: language || 'cpp',
      mode: mode || 'practice',
      isSubmitted: Boolean(isSubmitted),
      type: 'hint'
    });

    res.json(response);
  } catch (error: any) {
    console.error('aiRoutes /hint error:', error);
    res.status(500).json({ error: 'AI hint service unavailable' });
  }
});

// POST /api/ai/explain - Quick Action: Explain error or post-submission bug
router.post('/explain', async (req: Request, res: Response) => {
  try {
    const { questionId, userCode, executionOutput, language, mode, isSubmitted } = req.body;
    if (!questionId) return res.status(400).json({ error: 'questionId is required' });

    const promptMessage = isSubmitted
      ? 'Please provide a comprehensive explanation of the bug, why my code failed or passed, and the correct approach.'
      : 'Please explain this compiler or execution error and how to fix syntax or boundary mistakes.';

    const response = await aiService.handleChat({
      questionId,
      message: promptMessage,
      userCode,
      executionOutput,
      language: language || 'cpp',
      mode: mode || 'practice',
      isSubmitted: Boolean(isSubmitted),
      type: isSubmitted ? 'explanation' : 'error-help'
    });

    res.json(response);
  } catch (error: any) {
    console.error('aiRoutes /explain error:', error);
    res.status(500).json({ error: 'AI explain service unavailable' });
  }
});

// POST /api/ai/review - Quick Action: Review my approach
router.post('/review', async (req: Request, res: Response) => {
  try {
    const { questionId, userCode, executionOutput, language, mode, isSubmitted } = req.body;
    if (!questionId) return res.status(400).json({ error: 'questionId is required' });

    const promptMessage = 'Please review my current code structure and approach. Highlight any potential state or algorithmic flaws without spoiling the exact solution.';

    const response = await aiService.handleChat({
      questionId,
      message: promptMessage,
      userCode,
      executionOutput,
      language: language || 'cpp',
      mode: mode || 'practice',
      isSubmitted: Boolean(isSubmitted),
      type: 'review'
    });

    res.json(response);
  } catch (error: any) {
    console.error('aiRoutes /review error:', error);
    res.status(500).json({ error: 'AI review service unavailable' });
  }
});

export default router;
