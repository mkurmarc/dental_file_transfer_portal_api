from fastapi import Form, UploadFile, File
from pydantic import BaseModel, EmailStr, Field, SecretStr, validator
from typing import Optional

'''auth routes''' 
# incoming - user login info
class UserLogin(BaseModel):
    email: EmailStr
    password: str


'''user routes'''
# incoming - create user info
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    email: EmailStr
    password: str
    confirm_password: str

    class Config:
        fields = {
            'confirm_password':{
            'exclude': ...,
            }
        }
        min_anystr_length = 1
        max_anystr_length = 50
        error_msg_templated = {
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }
        anystr_strip_whitespace = True

    @validator('password')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

    # class Config: 
    #     json_encoders = { # To be able to send SecretStr in a response model
    #         SecretStr: lambda v: v.get_secret_value() if v else None
    #     }

'''/upload-files POST'''
# incoming - files and names assoc
class Upload(BaseModel):
    patient_first_name: str = Form(...)
    patient_last_name: str = Form(...)
    file_name: str = Form(...)
    files: list[UploadFile] = File(..., description="Upload muitiple files") 

    ''' using UploadFile without bytes means the file will be saved in spooled memory in background which
    is faster than uploading file using bytes. Can also save it to fastapi server, and can read and write 
    the file.'''

'''/login GET'''
# outgoing
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

"""
'''admin routes'''
# incoming  
class AdminDownload(BaseModel):
    # custom data type for files
"""
