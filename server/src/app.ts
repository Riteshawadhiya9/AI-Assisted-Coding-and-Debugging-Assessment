import path from 'path';
import fs from 'fs';
import dotenv from 'dotenv';

// Load .env before importing routes so all child modules have access to process.env
const envCandidatePaths = [
  path.join(__dirname, '..', '.env'),
  path.join(process.cwd(), '.env'),
  path.join(process.cwd(), 'server', '.env')
];

for (const envPath of envCandidatePaths) {
  if (fs.existsSync(envPath)) {
    dotenv.config({ path: envPath });
    break;
  }
}

import express from 'express';
import cors from 'cors';
import questionRoutes from './routes/questionRoutes';
import aiRoutes from './routes/aiRoutes';
import codingRoutes from './routes/codingRoutes';

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Routes — Debugging Assessment
app.use('/api/questions', questionRoutes);
app.use('/api/ai', aiRoutes);

// Routes — AI-Assisted Coding
app.use('/api/coding', codingRoutes);

// Health Check Endpoint
app.get('/api/health', (req, res) => {
  res.json({ ok: true });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

export default app;
