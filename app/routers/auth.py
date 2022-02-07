from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
# from .. import database, schemas, models, utils, oauth2


router = APIRouter(tags=['Authentication'])


@router.get('/login')
def get_login_page():
    return


@router.post('/login', )
def login():
    return  #return token