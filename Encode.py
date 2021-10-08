import cv2
import os
import base64
from stegano import lsb
from subprocess import call, STDOUT
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


print("Cryptography Based Image/Vide Steganography for more secure data hiding")
print("ENCODING MODULE")
print("1.Hide Message in Image")
print("2.Hide Message in Video")

choice = input()

if choice == '1':
    print("Enter Image Path")
    img_path = input()
    print("Enter Message")
    message = input()
    print("Encoding...")
    secret=lsb.hide(img_path,message)
    secret.save('./encoded_image.png')
    print("Completed.....")

elif choice == '2':
    print("Encrypting...")
    password_provided = "aplhaaplha"
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
    print ("Encryption-Key:")
    print (key)
    file = open('Encryption_key.key','wb')
    file.write(key)
    file.close()

    txt = Path('message.txt').read_text()
    txt = txt.replace('\n','')
    encoded = txt.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    # print (encrypted)
    file = open('Encrypted_message.txt','wb')
    file.write(encrypted)
    file.close()

    print("Cipher-Text:")
    print(encrypted)
    def split(word):
        return [char for char in word]

    call(["ffmpeg", "-i","video.mp4" , "-q:a", "0", "-map", "a", "temp_folder/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)

    print("Extracting frams from the video...")
    vidcap = cv2.VideoCapture("video.mp4")
    count=0
    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join("temp_folder", "{:d}.png".format(count)), image)
        count += 1

    print("Embedding the Encrypted text in frames...")
    txt = Path('Encrypted_message.txt').read_text()
    txt = txt.replace('\n','')
    str = split(txt)
    for i in range(0,len(str)):
        f_name = "{}{}.png".format("temp_folder/",i)
        secret = lsb.hide(f_name,str[i])
        secret.save(f_name)
        print("[INFO] frame {} holds {}".format(f_name,str[i]))

    print("Compiling the video...")
    call(["ffmpeg", "-i", "temp_folder/%d.png" , "-vcodec", "png", "video.mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)

    call(["ffmpeg", "-i", "video.mov", "-i", "temp_folder/audio.mp3", "-codec", "copy","data/enc-" +"final"+".mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
    print("Completed.")
else:
    print("Invalid Choice!")
