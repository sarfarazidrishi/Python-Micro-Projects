import qrcode as qr

img=qr.make("""Faraz loves aiza""")
img.save("greet1.png")
""".save is a method or qrcode module and 
the string in .save it the name with which
you want to save the qr code"""