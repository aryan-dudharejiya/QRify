print("Hey, you can make QR code from your links now!")
a = input("Enter your link here: ")
print("NOTE: don't forget to type .png at the end of your qr code's name")
b = input("Enter your qrcode's name :")

import qrcode as qr
img= qr.make(a)
img.save(b)


