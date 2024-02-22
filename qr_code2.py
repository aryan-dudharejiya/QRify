c = input("Enter your link here : ")
print("NOTE: don't forget to type .png at the end of your qr code's name")
f = input("Enter your qrcode's name here : ")
d = input("Enter your filling color : ")
e = input("Enter your background color : ")


import qrcode
from PIL import Image


qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4,)
qr.add_data(f)
qr.make(fit=True)
img=qr.make_image(fill_color=d, back_color=e)
img.save(f)

print("Thank you for using our function!😊")