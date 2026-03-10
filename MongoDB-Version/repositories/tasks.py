from models import Priority, Task, CreateTask, UpdateTask
import database as db


def get_all(completed: bool | None = None, priority: Priority | None = None) -> list[Task]:
    result = db.tasks

    if completed is not None:
        result = [task for task in result if task.completed == completed]
    
    if priority is not None:
        result = [task for task in result if task.priority == priority]

    return result

def get_by_id(id: int) -> Task | None:
    for task in db.tasks:
        if task.id == id:
            return task
    return None

def create(task: CreateTask) -> Task:
    new_task = Task(id=db.next_id, **task.model_dump())
    db.tasks.append(new_task)
    db.next_id += 1
    return new_task

def update(id: int, task: CreateTask) -> Task | None:
    new_task = Task(id=id, **task.model_dump())
    for i, existing_task in enumerate(db.tasks):
        if existing_task.id == id:
            db.tasks[i] = new_task
            return new_task
    return None

def patch(id: int, task: UpdateTask) -> Task | None:
    for i, existing_task in enumerate(db.tasks):
        if existing_task.id == id:
            updates = task.model_dump(exclude_unset=True)
            updated_task = existing_task.model_copy(update=updates)
            db.tasks[i] = updated_task
            return updated_task
    return None

def delete(id: int) -> bool:
    for i, existing_task in enumerate(db.tasks):
        if existing_task.id == id:
            db.tasks.pop(i)
            return True
    return False