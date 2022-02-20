from fastapi import APIRouter, File, Depends
from fastapi.responses import HTMLResponse
from fastapi import UploadFile
from sqlalchemy.orm import Session
from ..static import html_generator
from .. import database, schemas, models, utils, oauth2



router = APIRouter(
    prefix='/file',
    tags=['Upload Files']
)


@router.get("/", response_class=HTMLResponse)
async def get_upload_page(upload: schemas.Upload, current_user: int = Depends(oauth2.get_current_user)):

    return html_generator.gen_upload()


@router.post("/")
async def create_upload_file(
    files: list[UploadFile] = File(..., description="Upload muitiple files")
):

    return {"filenames": [file.filename for file in files]}
    # { "filenames": [filename1, filename2, filename3, ...] }



'''
# Use StreamingResponse to iterate over file object 

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

some_file_path = "large-video-file.mp4"
app = FastAPI()


@app.get("/")
def main():
    def iterfile():  # 
        with open(some_file_path, mode="rb") as file_like:  # 
            yield from file_like  # 

    return StreamingResponse(iterfile(), media_type="video/mp4")

'''