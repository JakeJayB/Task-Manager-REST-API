from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.home import router as home_router
from routers.tasks import router as task_router
import database as db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(home_router)
app.include_router(task_router)