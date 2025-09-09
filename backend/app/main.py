from fastapi import FastAPI
from .routers import tasks, projects

app = FastAPI(title="Knowledge Hub API")

app.include_router(tasks.router)
app.include_router(projects.router)

@app.get("/")
async def root():
    return {"msg": "Knowledge Hub API running"}
