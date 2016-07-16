from openpyxl import Workbook
from openpyxl.drawing.image import Image
# pip install pillow

wb = Workbook()
ws = wb.active

img = Image('image.png')
ws.add_image(img, 'A1')

wb.save('image_example.xlsx')
