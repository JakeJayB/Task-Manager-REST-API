# Script Purpose: Client connection to the Task Manager database

from pymongo import AsyncMongoClient
from config import settings

async def main():
    
    client = AsyncMongoClient(settings.MONGODB_URI)

    names = await client.list_database_names()

    for name in names:
        print(name)
    db = client[settings.DB_NAME]


    collection = db.get_collection('Tasks')

    print(collection)


import asyncio
asyncio.run(main())