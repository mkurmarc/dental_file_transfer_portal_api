from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
# from .. import database, schemas, models, utils, oauth2


router = APIRouter(
    prefix="/login",
    tags=['Authentication'])


@router.get('/')
def get_login_page():
    return


@router.post('/')
def login():
    return  #return token