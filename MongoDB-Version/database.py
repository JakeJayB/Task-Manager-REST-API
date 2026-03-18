# Script Purpose: Client connection to the Task Manager database

from pymongo import AsyncMongoClient
from pymongo.errors import PyMongoError
from config import settings
    
client: AsyncMongoClient = AsyncMongoClient(settings.MONGODB_URI)

async def connect():
    print("Connecting to MongoDB...")
    try:
        await client.admin.command("ping")
        print("MongoDB Connection Successful")
    except PyMongoError as e:
        print(f"MongoDB connection failed: {e}")
        raise  


async def disconnect():
    print("Closing MongoDB Connection...")
    if client is not None:
        await client.close()
    print("MongoDB Connection Successfully Closed")


def get_task_collection():
    return client[settings.DB_NAME][settings.COLLECTION_NAME]