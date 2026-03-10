
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get('/', response_class=HTMLResponse, include_in_schema=False)
def init():
    return "<h1>Welcome to the home page!</h1>\n<p>go to http://127.0.0.1:8000/docs to interact with the API routes</p>"