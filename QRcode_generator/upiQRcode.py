import qrcode
from PIL import Image

qr=qrcode.QRCode(
    version=1,
    border=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10
)

address=input("Enter upi id: ")
print("generating")

qr.add_data(f"{address}")

qr.make(fit=True)

image=qr.make_image(
    fill_color="blue", #Qr code color
    back_color="yellow" #background_color
)

logo=Image.open("salambhai.png").convert("RGBA") 
logo_size=200 #size in pixel
logo=logo.resize((logo_size, logo_size))
image.paste(logo, ((image.size[0]-logo.size[0])//2, (image.size[1]-logo.size[1]-120)))

image.save("salam.jpg")
image.show()

