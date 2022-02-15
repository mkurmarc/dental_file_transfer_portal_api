import email
from pydantic import BaseModel, EmailStr, FilePath, SecretStr

'''auth routes''' 
# incoming POST - user login info
class UserLogin(BaseModel):
    email: EmailStr
    password: SecretStr


'''user routes'''
# incoming POST - create user info
class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    confirm_email: EmailStr
    password: SecretStr
    confirm_password: SecretStr
    isAccepted: bool

'''upload_files routes'''
# incoming POST - files and names assoc
class Upload(BaseModel):
    first_name: str
    last_name: str
    # custom data type for files

