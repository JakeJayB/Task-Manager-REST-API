from fastapi import status, APIRouter
from models import Task, CreateTask, UpdateTask, Priority
from typing import Optional
import services.tasks as task_service
import asyncio

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.get('/', response_model=list[Task])
def get_all_tasks(completed: Optional[bool] = None, priority: Optional[Priority] = None):
    return task_service.get_all(completed, priority)

@router.get('/{id}', response_model=Task)
async def get_task(id: str):
    return await task_service.get_by_id(id)

@router.post('/', response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: CreateTask):
    return await task_service.create(task)

@router.put('/{id}', response_model=Task)
def update_task(id: int, task: CreateTask):
    return task_service.update(id, task)

@router.patch('/{id}', response_model=Task)
def patch_task(id: int, task: UpdateTask):
    return task_service.patch(id, task)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    task_service.delete(id)