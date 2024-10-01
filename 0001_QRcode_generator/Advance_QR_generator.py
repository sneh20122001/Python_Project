import qrcode as qr
from PIL import Image


qr_change = qr.QRCode(box_size=10,border=4)

qr_change.add_data("https://www.youtube.com/watch?v=GPVsHOlRBBI") # data analysis course 

qr_change.make(fit=True)
img = qr_change.make_image(fill_color = "white",back_color="black")
img.save("Adv_QR.png")