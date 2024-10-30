#this section of program : text_to_handwriting relies on an api that's pywhatkit api to  get font ot convert to handweitten format, it may not work sometimes
#______________program 1 starts_______________
# import pywhatkit as kit

# text="""This approach gives you a basic text
# -to-handwriting conversion. Let me know if you'd
# like to customize the handwriting style further or 
# add other features!"""

# kit.text_to_handwriting(text, save_to="testing1.jpg", rgb=(0, 0, 240))
#______________program 1 ends here _______________


#-------------------program 2 starts here--------------------
from PIL import Image, ImageDraw, ImageFont

text="I am yours. Dont't give myself back to me \n                                                            -Rumi"

"""image is variable that stores basic data(canvas or background) for image , creacted by Image.new(),
this function from pillow library creates new image, 
RGB: this declares mode of image
(other modes are 1. L=grayscale, 2. rbga=red green blue alpha, this suited for transparent images, 3. 1= binary(black and white),
4.cmyk=Stands for Cyan, Magenta, Yellow, and Black, primarily used for printing suited for images meant for printed media) """

image=Image.new('RGB', (500, 700), color="white")

#use => image=Image.open("localimage.jpg") this if you have image and wants to add text to it
# image=Image.open("localimage.jpg")

draw=ImageDraw.Draw(image) #initialize the drawing on image (backgrond for image to be created)

#try except block try to open font file, if it is not there or incorrct then defalut font will be assigned to font variavle
try:
    font=ImageFont.truetype("Creattion Demo.otf", 40) #30 is font size
    print("this font")
except IOError:
    font=ImageFont.load_default()
    
x,y= 85, 280 #position of text on image
line_height= 30
#text.splitlines() breaks the para into lines based on \n
for line in text.splitlines():
    draw.text((x, y), line, font=font, fill=(0, 0, 0)) #text color
    y+=line_height # new line postion of text across axis (vertical poition)
    
image.save('test3.jpg') #save image with test1.jpg name in working folder
image.show()