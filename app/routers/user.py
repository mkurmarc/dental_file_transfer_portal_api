from sys import prefix
from fastapi import status, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session


# prefix = adds the string to the beginning of each path op
# tags = is for the docs website for this api, it groups these path ops under 'Users' in the docs
router = APIRouter(
    prefix="/users", 
    tags=['Users'] 
)

# path op GETs the create user page to render
@router.get("/create_user") 
def create_user():
    
    return

# path op when user is done filling out form and hits 'done' button
@router.post('/create_user')
def get_create_page():
    return 