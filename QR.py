import qrcode
qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
data = "Hello, World!"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("qr_code.png")
