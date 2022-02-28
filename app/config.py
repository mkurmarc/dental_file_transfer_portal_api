from pydantic import BaseSettings
from fastapi.templating import Jinja2Templates
from pathlib import Path

''' this class allows for secure access to .ENV variables'''
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    f_key: str
    
    class Config:
        env_file = ".env"


settings = Settings()
# settings.database_password to access env variable


'''for jinja; I can import templates from whatever place in the app 
(sub-routers, main app, tests, ...) and not worry about directory paths.'''
base_directory = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(base_directory, 'templates')))