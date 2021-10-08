import cv2
import os
from stegano import lsb
from subprocess import call, STDOUT
from pathlib import Path
from base64 import decode
from cryptography.fernet import Fernet
# from pathlib import Path

file = open('Encryption_key.key','rb')
key = file.read()
file.close()


vidcap = cv2.VideoCapture("video.mov")
count=0
while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join("temp_folder2", "{:d}.png".format(count)), image)
        count += 1

secret=[]
str=""
root="temp_folder2/"
for i in range(len(os.listdir(root))):
    f_name="{}{}.png".format(root,i)
    secret_dec=lsb.reveal(f_name)
    if secret_dec == None:
        break
    secret.append(secret_dec)

str =''.join([i for i in secret])
# print(''.join([i for i in secret]))
# print(str)

f = Fernet(key)
str = bytes(str, 'utf-8')
decrypted = f.decrypt(str)
decoded = decrypted.decode()

file = open('Decrypted_message.txt','w+')
file.write(decoded)
file.close()
print(decoded)