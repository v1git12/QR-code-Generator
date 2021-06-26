import pyqrcode as qr
import png
from pyqrcode import QRCode
url = input("Enter The url to create QR code: ")
convertedQR = qr.create(url)
convertedQR.png("path",scale=8)
