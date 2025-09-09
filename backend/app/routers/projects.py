from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/")
async def list_projects():
    return [{"id": 1, "name": "Demo Project"}]

@router.post("/")
async def create_project(project: dict):
    return {"msg": "Project created", "project": project}
