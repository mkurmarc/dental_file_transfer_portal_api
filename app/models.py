from sqlalchemy import Column, Integer, LargeBinary, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, nullable=False)
    file = Column(LargeBinary, nullable=False)
    file_name = Column(String, nullable=False) # from UploadFile object
    content_type = Column(String, nullable=False)
    file_title = Column(String, nullable=False) # user input
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 
    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"),
                        nullable=False)
    owner = relationship("User") 
    

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, server_default='False', nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

