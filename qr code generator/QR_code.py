import os
import qrcode

img = qrcode.make("https://itimpactdeal.in/")

img.save("qr.png", "PNG")

os.system("display qr.png")