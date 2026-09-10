import { questionRepository } from '../services/questionRepository';
import { mockExecutionProvider } from '../services/execution/mockExecutionProvider';
import { QuestionValidator } from '../validators/questionValidator';
import { Question, Language, Topic, Difficulty } from '../types';

async function runUniversalQuestionBankTests() {
  console.log('=====================================================');
  console.log('🚀 RUNNING UNIVERSAL QUESTION BANK INTEGRATION TESTS');
  console.log('=====================================================\n');

  // -----------------------------------------------------------------
  // 1. TOTAL BANK SIZE & MULTI-TOPIC DISTRIBUTION
  // -----------------------------------------------------------------
  console.log('Test 1: Verifying total question bank size and topic quotas...');
  const allQuestions = questionRepository.getAll(false) as Question[];
  const totalCount = allQuestions.length;
  console.log(`  -> Found ${totalCount} total questions in question bank.`);

  if (totalCount < 60) {
    throw new Error(`Fail: Expected at least 60 questions, but found ${totalCount}`);
  }

  const topicCounts: Record<string, number> = {};
  const diffCounts: Record<string, number> = { easy: 0, medium: 0, hard: 0 };

  for (const q of allQuestions) {
    topicCounts[q.topic] = (topicCounts[q.topic] || 0) + 1;
    diffCounts[q.difficulty] = (diffCounts[q.difficulty] || 0) + 1;
  }

  console.log('  -> Topic Distribution:', topicCounts);
  console.log('  -> Difficulty Distribution:', diffCounts);

  if ((topicCounts['arrays'] || 0) < 10) {
    throw new Error(`Fail: Expected >= 10 Arrays questions, found ${topicCounts['arrays']}`);
  }
  if ((topicCounts['strings'] || 0) < 8) {
    throw new Error(`Fail: Expected >= 8 Strings questions, found ${topicCounts['strings']}`);
  }
  if ((topicCounts['hashmap'] || 0) < 6) {
    throw new Error(`Fail: Expected >= 6 HashMap questions, found ${topicCounts['hashmap']}`);
  }
  if ((topicCounts['trees'] || 0) < 10) {
    throw new Error(`Fail: Expected >= 10 Trees questions, found ${topicCounts['trees']}`);
  }
  if ((topicCounts['recursion'] || 0) < 6) {
    throw new Error(`Fail: Expected >= 6 Recursion questions, found ${topicCounts['recursion']}`);
  }
  if ((topicCounts['dp'] || 0) < 8) {
    throw new Error(`Fail: Expected >= 8 DP questions, found ${topicCounts['dp']}`);
  }
  if ((topicCounts['2ddp'] || 0) < 6) {
    throw new Error(`Fail: Expected >= 6 2D DP questions, found ${topicCounts['2ddp']}`);
  }
  if ((topicCounts['graphs'] || 0) < 10) {
    throw new Error(`Fail: Expected >= 10 Graphs questions, found ${topicCounts['graphs']}`);
  }

  console.log('✔ Test 1 Passed: Question bank sizes and distributions satisfy all category requirements.\n');

  // -----------------------------------------------------------------
  // 2. LANGUAGE INDEPENDENCE & IMPLEMENTATION PARITY (C, C++, JAVA)
  // -----------------------------------------------------------------
  console.log('Test 2: Verifying 100% language independence and implementation completeness...');
  const languages: Language[] = ['c', 'cpp', 'java'];
  
  for (const q of allQuestions) {
    if (!q.implementations) {
      throw new Error(`Fail: Question ${q.id} is missing multi-language implementations container!`);
    }

    for (const lang of languages) {
      const impl = q.implementations[lang];
      if (!impl) {
        throw new Error(`Fail: Question ${q.id} is missing implementation for language '${lang}'!`);
      }
      if (!impl.buggyCode || impl.buggyCode.trim() === '') {
        throw new Error(`Fail: Question ${q.id} has empty buggyCode for language '${lang}'!`);
      }
      if (!impl.correctCode || impl.correctCode.trim() === '') {
        throw new Error(`Fail: Question ${q.id} has empty correctCode for language '${lang}'!`);
      }
    }

    // Shared problem statement, test cases, and constraints verification
    if (!q.problemStatement || q.problemStatement.trim() === '') {
      throw new Error(`Fail: Question ${q.id} has empty problem statement.`);
    }
    if (!Array.isArray(q.visibleTestCases) || q.visibleTestCases.length === 0) {
      throw new Error(`Fail: Question ${q.id} has no visible test cases.`);
    }
    if (!Array.isArray(q.hiddenTestCases) || q.hiddenTestCases.length === 0) {
      throw new Error(`Fail: Question ${q.id} has no hidden test cases.`);
    }
  }
  console.log(`✔ Test 2 Passed: All ${allQuestions.length} questions contain complete, independent implementations in C, C++, and Java.\n`);

  // -----------------------------------------------------------------
  // 3. SCHEMA & INTEGRITY VALIDATION (QuestionValidator)
  // -----------------------------------------------------------------
  console.log('Test 3: Schema and quality validation via QuestionValidator...');
  const validationResult = QuestionValidator.validateQuestionBank(allQuestions);
  if (!validationResult.isValid) {
    console.error('Validation errors:', validationResult.errorsByQuestion);
    throw new Error(`Fail: ${validationResult.invalidCount} questions failed schema validation.`);
  }
  console.log(`✔ Test 3 Passed: All ${validationResult.validCount} questions strictly adhere to Question schema.\n`);

  // -----------------------------------------------------------------
  // 4. SANITIZATION & LEAK PREVENTION ACROSS ALL LANGUAGES
  // -----------------------------------------------------------------
  console.log('Test 4: Sanitization and solution/hidden test protection...');
  const sanitizedList = questionRepository.getAll(true);
  for (const q of sanitizedList as any[]) {
    if ('correctCode' in q && q.correctCode !== undefined) {
      throw new Error(`Fail: Sanitized question ${q.id} leaked top-level 'correctCode'!`);
    }
    if (q.implementations) {
      for (const lang of languages) {
        if ('correctCode' in q.implementations[lang]) {
          throw new Error(`Fail: Sanitized question ${q.id} leaked implementations.${lang}.correctCode!`);
        }
        if (!q.implementations[lang].buggyCode) {
          throw new Error(`Fail: Sanitized question ${q.id} missing implementations.${lang}.buggyCode!`);
        }
        // Verify buggy code has NO bug-revealing comments
        const bannedComment = /\/\/\s*(BUG|incorrect|fix|wrong|intentional|this causes|TODO)|\/\*[\s\S]*?(BUG|incorrect|fix|wrong|intentional|this causes|TODO)[\s\S]*?\*\//i;
        if (bannedComment.test(q.implementations[lang].buggyCode)) {
          throw new Error(`Fail: Question ${q.id} [${lang}] buggyCode contains forbidden bug-revealing comment!`);
        }
      }
    }
    if ('bugConcept' in q && q.bugConcept !== undefined) {
      throw new Error(`Fail: Sanitized question ${q.id} leaked 'bugConcept'!`);
    }
    if ('primaryBugType' in q && q.primaryBugType !== undefined) {
      throw new Error(`Fail: Sanitized question ${q.id} leaked 'primaryBugType'!`);
    }
    if ('explanation' in q && q.explanation !== undefined) {
      throw new Error(`Fail: Sanitized question ${q.id} leaked 'explanation'!`);
    }
    if (Array.isArray(q.hiddenTestCases) && q.hiddenTestCases.length > 0) {
      throw new Error(`Fail: Sanitized question ${q.id} leaked hiddenTestCases before submission!`);
    }
  }
  console.log('✔ Test 4 Passed: All sensitive solution and hidden test details are sanitized, and buggy code contains zero bug-revealing comments.\n');

  // -----------------------------------------------------------------
  // 5. MULTI-LANGUAGE MOCK EXECUTION (C, C++, JAVA)
  // -----------------------------------------------------------------
  console.log('Test 5: Multi-language MockExecutionProvider evaluation (C, C++, Java)...');
  const sampleQuestion = allQuestions.find(q => q.id === 'q_arr_kadane') || allQuestions[0];

  for (const lang of languages) {
    const impl = sampleQuestion.implementations[lang];
    
    // A. Execute with correct code for this language
    const execCorrect = await mockExecutionProvider.execute(impl.correctCode, sampleQuestion.id, {
      language: lang,
      isSubmission: false
    });
    if (!execCorrect.passed) {
      throw new Error(`Fail: Execution of correctCode for language ${lang} failed on question ${sampleQuestion.id}.`);
    }
    if (!execCorrect.testResults.every((t) => t.passed)) {
      throw new Error(`Fail: Not all tests passed for ${lang} correctCode.`);
    }

    // B. Execute with buggy code for this language
    const execBuggy = await mockExecutionProvider.execute(impl.buggyCode, sampleQuestion.id, {
      language: lang,
      isSubmission: false
    });
    if (execBuggy.passed) {
      throw new Error(`Fail: Execution of buggyCode for language ${lang} passed when it should fail.`);
    }

    // C. Execute with submission flag
    const execSubmit = await mockExecutionProvider.execute(impl.correctCode, sampleQuestion.id, {
      language: lang,
      isSubmission: true
    });
    if (!execSubmit.passed) {
      throw new Error(`Fail: Submission execution failed for ${lang} correctCode.`);
    }
  }
  console.log('✔ Test 5 Passed: MockExecutionProvider accurately evaluates code across C, C++, and Java.\n');

  // -----------------------------------------------------------------
  // 6. QUESTION REPOSITORY QUERY, FILTER & RANDOM SELECTION
  // -----------------------------------------------------------------
  console.log('Test 6: Compound query, filter, and random selection...');
  const randomC = questionRepository.getRandom({ language: 'c', topic: 'arrays' }, true) as any;
  if (!randomC || !randomC.implementations?.c) {
    throw new Error(`Fail: getRandom for c/arrays failed.`);
  }

  const queryResults = questionRepository.query({ topic: 'dp', difficulty: 'medium' }, true);
  if (queryResults.length === 0) {
    throw new Error(`Fail: query for dp/medium returned empty.`);
  }
  console.log(`✔ Test 6 Passed: Repository queries and random selections work reliably.\n`);

  console.log('=====================================================');
  console.log('🎉 ALL UNIVERSAL QUESTION BANK TESTS PASSED (6/6)');
  console.log('=====================================================');
}

runUniversalQuestionBankTests().catch((err) => {
  console.error('\n❌ QUESTION BANK TESTS FAILED:');
  console.error(err);
  process.exit(1);
});

