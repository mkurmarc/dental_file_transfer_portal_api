from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import UploadFile
from app.static.html_generator import gen_upload


router = APIRouter(
    tags=['Upload Files']
)


@router.get("/uploadfiles", response_class=HTMLResponse)
async def get_upload_page():
    return gen_upload()


@router.post("/uploadfiles")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}