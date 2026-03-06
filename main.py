from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Priority(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class CreateTask(BaseModel):
    title: str
    description: str
    completed: bool = False
    priority: Priority = 'low'

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    priority: Priority = 'low'
        
tasks : list[Task] = []
next_id = 1

@app.get('/')
def init():
    return "Welcome to the home page! go to http://127.0.0.1:8000/docs to interact with the API routes"

@app.post('/tasks', response_model=Task)
def create_task(task: CreateTask):
    global next_id
    
    new_task = Task(id=next_id, **task.model_dump())
    tasks.append(new_task)
    next_id += 1
    return new_task

@app.put('/tasks/{id}', response_model=Task)
def update_task(id: int, task: CreateTask):
    new_task = Task(id=id, **task.model_dump())

    for i, existing_task in enumerate(tasks):
        if existing_task.id == id:
            tasks[i] = new_task
            return new_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete('/tasks/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):

    for i, existing_task in enumerate(tasks):
        if existing_task.id == id:
            tasks.pop(i)
            return

    raise HTTPException(status_code=404, detail="Task not found")
 
@app.get('/tasks/{id}', response_model=Task)
def get_task(id: int):
    for task in tasks:
        if task.id == id:
            return task
    
    raise HTTPException(404, "Task not found")


@app.get('/tasks', response_model=list[Task])
def get_all_tasks():
    return tasks
