from tkinter import CASCADE
from sqlalchemy import Column, Integer, LargeBinary, String, Boolean, null
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, nullable=False)
    file = Column(LargeBinary, nullable=False)
    file_title = Column(String, nullable=False) 
    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"),
                        nullable=False)
    # user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User") 
    '''relationship automatically creates another property for File, so when we retrieve 
    File it will return an 'owner' property too, and it will figure out the relationship to   
    User. Basically, will fetch the User based of the owner id and return that for us'''
    ''' Example of data response with relationship:
    {
        "id": 12,
        "file": "",
        "file_title": "dfasdf",
        "patient_id": 3434,
        "user_id": 4545,
        "owner": {
            "id": 223,
            "first_name": "john",
            "last_name": "boomer",
            "email": "john@hotmail.com",
            "password": "fadfaf",
            "is_admin": False,
            "created_at": "2022"
        }
    }
    Use pydantic models in path operations to limit the data. For example changing the data
    format to only id and email, excluding the password and created_at properties.
    '''

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, server_default='TRUE', nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

