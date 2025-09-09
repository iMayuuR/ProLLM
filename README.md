# Project Knowledge Hub (Local LLM)

A ready-to-deploy system for logging daily tasks, sharing learnings, and generating docs per project.  
Runs fully local using Ollama + Chroma + FastAPI + Next.js.

## Quickstart
1. `docker compose up --build`
2. Open http://localhost:3000 for UI, API runs at http://localhost:8001


## Deploying to Render & Vercel

- Backend (Render): use the provided `backend/render.yaml`. Render will install `backend/requirements.txt` and run the `startCommand`.
- Frontend (Vercel): the `frontend/vercel.json` is configured for Vite; ensure the repo is connected and Vercel will run `npm run build` in `frontend`.

I added a minimal `backend/wsgi.py`, `backend/Procfile`, and `backend/app/__init__.py` so Gunicorn can find the FastAPI app. I also added a minimal Vite `src` entry so Vercel can build the frontend.

