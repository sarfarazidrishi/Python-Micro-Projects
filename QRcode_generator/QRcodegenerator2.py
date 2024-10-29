import qrcode
from PIL import Image

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10, #size of each box in QR code
    border=4, #thickness of border in QR code more value means smaller size of qr code and bigger border around the code
    )
address=input("Enter link or text you want to create QR for: ")
qr.add_data(f"{address}")
qr.make(fit=True) #fit=true :  adjust the size of qr code according to data passed in the .add_data
image=qr.make_image( #this method will create image
    fill_color="blue", #Qr code color
    back_color="yellow" #background_color
)

logo=Image.open("WhatsApp_Image_2024-10-29_at_10.16.04_5a91d627-removebg-preview.png").convert("RGBA") #.convert("rbga") add alpgha value, 3rd argument of .paste method it maintains transparency of logo
logo_size=250 #size in pixel 
logo=logo.resize((logo_size, logo_size)) #first value : width , second value: height
image.paste(logo, ((image.size[0]-logo.size[0])//2, (image.size[1]-logo.size[1])-40), logo)
""" comment for the line above: img.size[0] represents width of img and img.size[1]  represents height of img
similarly for logo and 
//2 two forward slashes are division it return non-float number 
if X/y gives 2.5 then use x//y it wil give only 2 (basically // return a whole number)
this helps better in positioning the image
"""

image.save("WhatsApp Image1 2024-10-291 at1 10.16.04_fc9b6fa6.jpg") #Hint : you can save it as linkedinlogo1.png to preserve transparency
image.show() #this method will open generated qr code default image view of your system