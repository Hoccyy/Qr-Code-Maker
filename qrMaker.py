import qrcode
#import sys

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=4)

# Add data to the QR code
data = input("Enter Data: ")

''' ~ remove the comment symbols from line 2 and here to avoid making blank Qrs or filter as you see fit
if len(data) == 0 or data == None:
    sys.exit()
'''

qr.add_data(data)

# Generate the QR code image
qr.make(fit=True)
try:
    img = qr.make_image(fill_color=input("Fill? : "), back_color=input("Background? (empty = Blank): "))
except:# Exception leave colors blank for faster usage
    img = qr.make_image(fill_color="black", back_color="white")

# Image saving
try:
    img.save(input("File Name? include photo extension such as  .jpg  or .png  etc."))
except:
    img.save("BarCode.png")