from fastapi import APIRouter, File, Depends, Form, UploadFile, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from ..static import html_generator
from .. import database, schemas, models, utils, oauth2, config


router = APIRouter(
    prefix='/file',
    tags=['Upload Files']
)


@router.get("/", response_class=HTMLResponse)
async def get_upload_page(request: Request, current_user: int = Depends(oauth2.get_current_user)):

    return config.templates.TemplateResponse("upload_files.html", {"request": request})


@router.post("/")
async def create_upload_file(current_user: int = Depends(oauth2.get_current_user),
patient_first_name: str = Form(...), patient_last_name: str = Form(...), 
file_title: str = Form(...), files: list[UploadFile] = File(..., description="Upload muitiple files"),
db: Session = Depends(database.get_db)):

    new_patient = models.Patient(first_name=patient_first_name, last_name=patient_last_name)
    db.add(new_patient)
    db.commit()
    
    files_to_add = []
    for file in files:
        bytes_file = await file.read()
        encrypted_file = utils.encrypt_file(bytes_file)
        new_file = models.File(file=encrypted_file, file_name=file.filename, 
                               content_type=file.content_type, file_title=file_title, 
                               user_id=current_user.id, patient_id=new_patient.id)
        files_to_add.append(new_file)                     
        await file.close()

    db.add_all(files_to_add)
    db.commit()
    # return html or something else to show success of file upload
    return {"status": "Success"} 


''' files[0].content_type
    return {"filenames": [file_title for file in files],
    "patient_first_name": [patient_first_name for file in files]}
    { "filenames": [filename1, filename2, filename3, ...] }
        
        
    print(patient_first_name + patient_last_name)
    print(files)
    file_content = await files.read()
    print(file_content)'''
