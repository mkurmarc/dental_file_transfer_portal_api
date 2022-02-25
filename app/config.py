from pydantic import BaseSettings

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
# settings.database_password 