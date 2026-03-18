from fastapi import HTTPException, status
from models import Task, CreateTask, UpdateTask, Priority
import repositories.tasks as task_repo

def get_all(completed: bool | None = None, priority: Priority | None = None) -> list[Task]:
    return task_repo.get_all(completed, priority)

async def get_by_id(id: str) -> Task | None:
    task = await task_repo.get_by_id(id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task
    
async def create(task: CreateTask) -> Task:
    return await task_repo.create(task)

def update(id: int, task: CreateTask) -> Task:
    updated_task = task_repo.update(id, task)
    if updated_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return updated_task

def patch(id: int, task: UpdateTask) -> Task:
    patched_task = task_repo.patch(id, task)
    if patched_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return patched_task

def delete(id: int) -> None:
    deleted = task_repo.delete(id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")