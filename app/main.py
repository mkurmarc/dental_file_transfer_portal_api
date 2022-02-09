from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from app.routers import auth, user
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory="app/static")


app = FastAPI()

app.mount(
    "/static", 
    StaticFiles(directory="app/static"),
    name="static"
)


app.include_router(user.router)
app.include_router(auth.router)

'''
USE JINJA, SEE STACK OVERFLOW SOLUTION

'''