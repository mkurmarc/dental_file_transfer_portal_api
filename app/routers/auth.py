from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.static.html_generator import gen_create_user, gen_login
# from .. import database, schemas, models, utils, oauth2


router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)


@router.get("/user", response_class=HTMLResponse) 
async def get_login_page():
    return gen_login()

# returns user upload page if credentials verfied
@router.post("/user") 
async def get_upload_page():
    return # gen_upload_page


@router.get("/admin", response_class=HTMLResponse) 
async def get_admin_login():
    return gen_login()

# returns admin page if credentials verfied
@router.post("/admin") 
async def get_upload_page():
    return # gen_upload_page