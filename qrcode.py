# Create QRCode image
# By Busyman.Inc

import pyqrcode

from PIL import Image
link = input("Enter anything to generate QR: ")
qr = pyqrcode.create(link)
qr.png("QRCode.png", scale=5)
Image.open("QRCode.png")
