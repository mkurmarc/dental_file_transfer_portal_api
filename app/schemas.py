from pydantic import BaseModel, EmailStr, SecretStr
from typing import Optional

'''auth routes''' 
# incoming - user login info
class UserLogin(BaseModel):
    email: EmailStr
    password: SecretStr


'''user routes'''
# incoming - create user info
class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    confirm_email: EmailStr
    password: SecretStr
    confirm_password: SecretStr
    isAccepted: bool

'''upload_files routes'''
# incoming - files and names assoc
class Upload(BaseModel):
    first_name: str
    last_name: str
    # custom data type for files

# incoming
class Token(BaseModel):
    access_token: str
    token_type: str

# outgoing
class TokenData(BaseModel):
    id: Optional[str] = None

"""
'''admin routes'''
# incoming  
class AdminDownload(BaseModel):
    # custom data type for files
"""
