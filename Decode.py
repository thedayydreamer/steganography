import cv2
import os
import base64
from base64 import decode
from stegano import lsb
from subprocess import call, STDOUT
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

print("Cryptography Based Image/Vide Steganography for more secure data hiding")
print("DECODING MODULE")
print("1.Reveal Message from Image")
print("2.Reveal Message from  Video")

choice = input()

if choice == '1':
    print("Enter Image Path")
    img_path = input()
    print("Extracting the message..")
    str = lsb.reveal(img_path)
    print(str)
    

elif choice == '2':
    print("Checking Encryption-key")
    file = open('Encryption_key.key','rb')
    key = file.read()
    file.close()

    print("Extracting frames from the video...")

    vidcap = cv2.VideoCapture("video.mov")
    count=0
    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join("temp_folder2", "{:d}.png".format(count)), image)
        count += 1

    print("Extracting the message from frames...")

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
    print("Cipher-text obtained:")
    print(str)
    print("Decrypting the message...")
    f = Fernet(key)
    str = bytes(str, 'utf-8')
    decrypted = f.decrypt(str)
    decoded = decrypted.decode()

    file = open('Decrypted_message.txt','w+')
    file.write(decoded)
    file.close()
    print("Hidden Message: "+decoded)
    print("Completed.")
else:
    print("Invalid Choice!")