from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from app.routers import auth, user

from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static", html=True), name="static")

app.include_router(user.router)
app.include_router(auth.router)

'''
USE JINJA, SEE STACK OVERFLOW SOLUTION

'''