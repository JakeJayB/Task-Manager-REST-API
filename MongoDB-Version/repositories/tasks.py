from models import Priority, Task, CreateTask, UpdateTask
from bson import ObjectId
import database as db


async def get_all(
    completed: bool | None = None, priority: Priority | None = None
) -> list[Task]:
    tasks = db.get_task_collection()
    query = {}

    if completed is not None:
        query["completed"] = completed

    if priority is not None:
        query["priority"] = priority

    return await tasks.find(query).to_list()

async def get_by_id(id: str) -> Task | None:
    collection = db.get_task_collection()
    doc = await collection.find_one({"_id": ObjectId(id)})
    return Task(**doc) if doc else None

async def create(task: CreateTask) -> Task:
    collection = db.get_task_collection()
    doc = await collection.insert_one(task.model_dump())
    doc = await collection.find_one({"_id": doc.inserted_id})
    return Task(**doc)

async def update(id: str, task: CreateTask) -> Task | None:
    from pymongo.collection import ReturnDocument

    tasks = db.get_task_collection()
    doc = await tasks.find_one_and_replace(
        {"_id": ObjectId(id)}, task.model_dump(), return_document=ReturnDocument.AFTER
    )
    return Task(**doc) if doc else None

async def patch(id: str, task: UpdateTask) -> Task | None:
    from pymongo.collection import ReturnDocument

    tasks = db.get_task_collection()
    doc = await tasks.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": task.model_dump(exclude_unset=True)},
        return_document=ReturnDocument.AFTER
    )
    return Task(**doc) if doc else None

async def delete(id: str) -> bool:
    tasks = db.get_task_collection()
    response = await tasks.delete_one({"_id": ObjectId(id)})
    return response.deleted_count == 1
