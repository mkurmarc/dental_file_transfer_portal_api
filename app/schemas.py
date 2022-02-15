from pydantic import BaseModel, EmailStr

# user routes
class UserLogin(BaseModel):
    email: EmailStr
    password: str

