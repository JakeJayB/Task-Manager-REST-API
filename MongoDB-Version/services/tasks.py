from fastapi import HTTPException, status
from models import Task, CreateTask, UpdateTask, Priority
from bson import ObjectId
import repositories.tasks as task_repo

async def get_all(completed: bool | None = None, priority: Priority | None = None) -> list[Task]:
    return await task_repo.get_all(completed, priority)

async def get_by_id(id: str) -> Task | None:
    id = id.strip()
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"'{id}' is not a valid ObjectId")
     
    task = await task_repo.get_by_id(id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task
    
async def create(task: CreateTask) -> Task:
    return await task_repo.create(task)

async def update(id: str, task: CreateTask) -> Task:
    id = id.strip()
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"'{id}' is not a valid ObjectId")
    
    updated_task = await task_repo.update(id, task)
    if updated_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return updated_task

async def patch(id: str, task: UpdateTask) -> Task:
    id = id.strip()
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"'{id}' is not a valid ObjectId")
    
    patched_task = await task_repo.patch(id, task)
    if patched_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return patched_task

async def delete(id: str) -> None:
    id = id.strip()
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"'{id}' is not a valid ObjectId")
    
    deleted = await task_repo.delete(id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")