from stegano import lsb
from pathlib import Path

#message encoding
txt = Path('message.txt').read_text()
txt = txt.replace('\n','')
secret=lsb.hide('./image.png',txt)
secret.save('./encoded_image.png')

# #message decoding
# str = lsb.reveal('./encoded_image.png')
# f = open("decodec_message.txt","x")
# f.write(str)
# # print (str)
# f.close()






