from models import Priority, Task, CreateTask, UpdateTask
from bson import ObjectId
import database as db


def get_all(completed: bool | None = None, priority: Priority | None = None) -> list[Task]:
    result = db.tasks

    if completed is not None:
        result = [task for task in result if task.completed == completed]
    
    if priority is not None:
        result = [task for task in result if task.priority == priority]

    return result

# def get_by_id(id: int) -> Task | None:
#     for task in db.tasks:
#         if task.id == id:
#             return task
#     return None


async def get_by_id(id: str) -> Task | None:
    collection = db.get_task_collection()
    doc = await collection.find_one({"_id" : ObjectId(id)})
    return Task(**doc) if doc else None

# def create(task: CreateTask) -> Task:
#     new_task = Task(id=db.next_id, **task.model_dump())
#     db.tasks.append(new_task)
#     db.next_id += 1
#     return new_task

async def create(task: CreateTask) -> Task:
    collection = db.get_task_collection()
    doc = await collection.insert_one(task.model_dump())
    doc = await collection.find_one({'_id' : doc.inserted_id})
    return Task(**doc)
    

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