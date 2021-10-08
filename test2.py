from base64 import decode
from cryptography.fernet import Fernet
from pathlib import Path

file = open('Encryption_key.key','rb')
key = file.read()
file.close()

file = open('Encrypted_message.txt','rb')
encrypted_message = file.read()
file.close

f = Fernet(key)
decrypted = f.decrypt(encrypted_message)
decoded = decrypted.decode()
# print(decoded)

file = open('Decrypted_message.txt','w+')
file.write(decoded)
file.close()
