from fastapi import status, Depends, APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from ..static import html_generator
from .. import database, schemas, models, utils, oauth2

# prefix = adds the string to the beginning of each path op
# tags = is for the docs website for this api, it groups these path ops under 'Users' in the docs
router = APIRouter(
    prefix="/user", 
    tags=['User']
)

'''FIX: How do i send an email for user registration?'''
# path op GETs the create user page to render
@router.get("/", response_class=HTMLResponse) 
async def get_create_page():
    return html_generator.gen_create_user()


# creates new user
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict()) # convert 'user' to dictionary, then unpack it into SQLAlchemy model
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
