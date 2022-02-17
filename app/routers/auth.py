from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
# from app.schemas import UserLogin
from app.static.html_generator import gen_create_user, gen_login, gen_upload
from .. import database


router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)

# returns login view
@router.get("/", response_class=HTMLResponse) 
async def get_login_page():
    return gen_login()

# returns user upload page if credentials verfied
@router.post("/") 
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(database.get_db)
):
    if True: # creds and isUser are true
        return HTMLResponse(gen_upload)
      
    return RedirectResponse("http://127.0.0.1:8000/login", status_code=302)
