from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
async def list_tasks():
    return [{"id": 1, "name": "Sample Task"}]

@router.post("/")
async def create_task(task: dict):
    return {"msg": "Task created", "task": task}
