from fastapi import APIRouter, File
from fastapi.responses import HTMLResponse
from app.static.html_generator import gen_admin_dashboard
from .. import schemas


router = APIRouter(
    prefix="/admin",
    tags=["Administrator"]
)

# routes for admin only users
@router.get("/", response_class=HTMLResponse)
async def get_admin_dashboard(token: schemas.Token):
    # if token valid    
    return gen_admin_dashboard()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}



'''
# Use FileResponse to return files when admin user downloads file(s)

from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "large-video-file.mp4"
app = FastAPI()


@app.get("/", response_class=FileResponse)
async def main():
    return some_file_path

'''