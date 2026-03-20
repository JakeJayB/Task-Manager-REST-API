from fastapi import status, APIRouter
from models import Task, CreateTask, UpdateTask, Priority
from typing import Optional
import services.tasks as task_service

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.get('/', response_model=list[Task])
async def get_all_tasks(completed: Optional[bool] = None, priority: Optional[Priority] = None):
    return await task_service.get_all(completed, priority)

@router.get('/{id}', response_model=Task)
async def get_task(id: str):
    return await task_service.get_by_id(id)

@router.post('/', response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: CreateTask):
    return await task_service.create(task)

@router.put('/{id}', response_model=Task)
async def update_task(id: str, task: CreateTask):
    return await task_service.update(id, task)

@router.patch('/{id}', response_model=Task)
async def patch_task(id: str, task: UpdateTask):
    return await task_service.patch(id, task)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: str):
    await task_service.delete(id)