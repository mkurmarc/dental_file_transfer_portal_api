from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.schemas import UserLogin
from app.static.html_generator import gen_create_user, gen_login
# from .. import database, schemas, models, utils, oauth2


router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)


@router.get("/", response_class=HTMLResponse) 
async def get_login_page():
    return gen_login()

# returns user upload page if credentials verfied
@router.post("/") 
async def login(user_credentials: UserLogin, ):
    return # gen_upload_page



'''
EXAMPLE:
@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter( # '.username' here because OAuth2PasswordRequestForm  
        models.User.email == user_credentials.username).first() # saves the data under that variable name
                                                                                                             
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id}) #create a token

    return {"access_token": access_token, "token_type": "bearer"} #return token
'''