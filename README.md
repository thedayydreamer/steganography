# steganography
Cryptography based Image/Video Steganography for Data Hiding
this is a linux based terminal application which performs data/information hiding in a image/video file
to embedd a file(image/video) with image/video:
run encode file using linux terminal
input the path of the image/video
enter the text(information/data) which is to be hide
it will perform encryption and will create a key
then it will create another file (image/video) with embedded information/data, which can be transfered.

to reveal the information/data from the embedded file:
run decode file using linux terminal
input the path of the embedded file with encryption key
it will extract the hidden messsage
and it will perform decryption with the provided key
if the encryption key is right it will create an output file with the embedded message
