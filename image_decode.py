from stegano import lsb
from pathlib import Path

# #message decoding
str = lsb.reveal('./encoded_image.png')
f = open("decodec_message_from_image.txt","x")
f.write(str)
print (str)
f.close()
