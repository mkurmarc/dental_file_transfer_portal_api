from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import auth, upload_files, user
from app.internal import admin
from app.schemas import Upload
from .database import engine
from . import models
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.static.html_generator import gen_home
from fastapi.responses import HTMLResponse


# BASE_PATH = Path(__file__).resolve().parent
# TEMPLATES = Jinja2Templates(directory="app/static")
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount(
    "/static", 
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(upload_files.router)
app.include_router(admin.router)

# Home Page - temporary
@app.get("/", response_class=HTMLResponse) 
async def get_home():
    print(Upload.schema_json(indent=2))
    return gen_home()
