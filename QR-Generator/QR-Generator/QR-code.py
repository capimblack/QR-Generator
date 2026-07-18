import qrcode

url: str = input("What will be the destination of the QR code? ")

img = qrcode.make(url)
img.save("qrcode.png")

from pathlib import Path

pt = Path(__file__).parent.resolve()

cmh = pt / "qrcode.png"

print(f"Your QR code is here: {cmh}")