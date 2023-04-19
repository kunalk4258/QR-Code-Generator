import qrcode

data = 'Hey this is my QR'

img = qrcode.make(data)

img.save('C:\Users\KIIT\OneDrive\Documents\Programming\Python\Projects\myqrcode.png')
