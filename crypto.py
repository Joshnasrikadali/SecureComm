import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_data, password):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    f = Fernet(key)
    encrypted = f.encrypt(file_data)
    return salt + encrypted

def decrypt_file(file_data, password):
    salt = file_data[:16]
    encrypted = file_data[16:]
    key = generate_key(password, salt)
    f = Fernet(key)
    return f.decrypt(encrypted)