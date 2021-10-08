import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import Path

password_provided = "password"
password = password_provided.encode()

salt = b'&\xb8\xd9\xa5\x92\x00Pl\x92Y\xf6\xd8#\x92\xcdC'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) 
# print (key)
file = open('Encryption_key.key','wb')
file.write(key)
file.close()

txt = Path('message.txt').read_text()
txt = txt.replace('\n','')
encoded = txt.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)
print (encrypted)
file = open('Encrypted_message.txt','wb')
file.write(encrypted)
file.close()
