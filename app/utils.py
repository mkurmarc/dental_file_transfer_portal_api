from passlib.context import CryptContext
from passlib.context import CryptContext
from cryptography.fernet import Fernet
from app.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hashes plain password 
def hash(password: str):
    return pwd_context.hash(password)

# verifies the user's input and the hashed password by hashing the user input and comparing
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# encrypts binary file
def encrypt_file(plain_file: bytes):
    f = Fernet(settings.f_key)
    encrypted_file = f.encrypt(plain_file)
    return encrypted_file

# decrypts the encrypted file
def decrypt_file(encrypted_file: bytes):
    f = Fernet(settings.f_key) 
    plain_binary_file = f.decrypt(bytes(encrypted_file))
    return plain_binary_file