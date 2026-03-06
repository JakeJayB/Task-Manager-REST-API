from fastapi import FastAPI
from routers.home import router as home_router
from routers.tasks import router as task_router

app = FastAPI()

app.include_router(home_router)
app.include_router(task_router)