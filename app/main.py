import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.routers import auth, upload_files, user
from app.internal import admin
from app.schemas import Upload
from .database import engine
from . import models, config
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.static.html_generator import gen_home
from fastapi.responses import HTMLResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# BASE_DIR = Path(__file__).resolve().parent
# templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

app.mount(
    "/static", 
    StaticFiles(directory="app/static"),
    name="static"
)

# templates = Jinja2Templates(directory=os.path.dirname(os.path.abspath(__file__)))


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(upload_files.router)
app.include_router(admin.router)

# Home Page - temporary
@app.get("/", response_class=HTMLResponse) 
async def get_login_page(request: Request):

    return config.templates.TemplateResponse("login.html", {"request": request})
