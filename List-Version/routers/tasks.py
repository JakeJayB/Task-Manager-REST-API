from fastapi import HTTPException, status, APIRouter
from models import Task, CreateTask, UpdateTask, Priority
import database as db
from typing import Optional

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.post('/', response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: CreateTask):    
    new_task = Task(id=db.next_id, **task.model_dump())
    db.tasks.append(new_task)
    db.next_id += 1
    return new_task

@router.put('/{id}', response_model=Task)
def update_task(id: int, task: CreateTask):
    new_task = Task(id=id, **task.model_dump())
    
    for i, existing_task in enumerate(db.tasks):
        if existing_task.id == id:
            db.tasks[i] = new_task
            return new_task

    raise HTTPException(status_code=404, detail="Task not found")

@router.patch('/{id}', response_model=Task)
def patch_task(id: int, task: UpdateTask):
    for i, existing_task in enumerate(db.tasks):
        if existing_task.id == id:
            updates = task.model_dump(exclude_unset=True)
            new_task =  existing_task.model_copy(update=updates)
            db.tasks[i] = new_task
            return new_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):

    for i, existing_task in enumerate(db.tasks):
        if existing_task.id == id:
            db.tasks.pop(i)
            return

    raise HTTPException(status_code=404, detail="Task not found")
 
@router.get('/{id}', response_model=Task)
def get_task(id: int):
    for task in db.tasks:
        if task.id == id:
            return task
    
    raise HTTPException(status_code=404, detail="Task not found")


@router.get('/', response_model=list[Task])
def get_all_tasks(completed: Optional[bool] = None, priority: Optional[Priority] = None):
    results = db.tasks
    
    if completed is not None:
        results = [task for task in results if task.completed == completed]
    if priority is not None:
        results = [task for task in results if task.priority == priority]

    return results
