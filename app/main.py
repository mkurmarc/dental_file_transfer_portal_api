from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.routers import auth, user
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)