import { Router } from 'express';
import { questionRepository } from '../services/questionRepository';
import { mockExecutionProvider } from '../services/execution/mockExecutionProvider';
import { Language, Topic, Difficulty } from '../types';

const router = Router();

// GET all questions or filtered questions (sanitized - no solutions or hidden tests)
router.get('/', (req, res) => {
  try {
    const language = req.query.language as Language | undefined;
    const topic = req.query.topic as Topic | undefined;
    const difficulty = req.query.difficulty as Difficulty | undefined;
    const search = req.query.search as string | undefined;

    if (language || topic || difficulty || search) {
      const list = questionRepository.query({ language, topic, difficulty, search }, true);
      return res.json(list);
    }

    const list = questionRepository.getAll(true);
    res.json(list);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve questions' });
  }
});

// GET a random question with optional filters (sanitized)
router.get('/random', (req, res) => {
  try {
    const language = req.query.language as Language | undefined;
    const topic = req.query.topic as Topic | undefined;
    const difficulty = req.query.difficulty as Difficulty | undefined;

    const question = questionRepository.getRandom({ language, topic, difficulty }, true);
    if (!question) {
      return res.status(404).json({ error: 'No question matches the specified criteria' });
    }
    res.json(question);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve random question' });
  }
});

// GET a question by ID (sanitized)
router.get('/:id', (req, res) => {
  try {
    const question = questionRepository.getById(req.params.id, true);
    if (!question) {
      return res.status(404).json({ error: 'Question not found' });
    }
    res.json(question);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve question' });
  }
});

// GET a question solution by ID (unsanitized - for post-submission explanations)
router.get('/:id/solution', (req, res) => {
  try {
    const question = questionRepository.getById(req.params.id, false);
    if (!question) {
      return res.status(404).json({ error: 'Question not found' });
    }
    res.json(question);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve solution details' });
  }
});

// POST to execute code against mock test cases
router.post('/:id/execute', async (req, res) => {
  try {
    const { code, language, isSubmission, userDiagnosis } = req.body;
    if (typeof code !== 'string') {
      return res.status(400).json({ error: 'Missing or invalid code body parameter' });
    }
    const result = await mockExecutionProvider.execute(code, req.params.id, {
      language: language as Language | undefined,
      isSubmission: !!isSubmission,
      userDiagnosis
    });
    res.json(result);
  } catch (error: any) {
    res.status(500).json({ error: error.message || 'Execution failed' });
  }
});


export default router;
