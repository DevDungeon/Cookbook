# pip install pillow
from PIL import ImageGrab

# Copy an image to your clipboard with CTRL-C before running
# to ensure an image is actually in your clipboard
img = ImageGrab.grabclipboard()

# Print image details
print(img)
# Example output:
# <PIL.BmpImagePlugin.DibImageFile image mode=RGB size=380x173 at 0x16A43064DA0>

# Save the image to disk
img.save('paste.png','PNG')
img.save('paste.jpg','JPEG')

# Store the bytes in a byte stream
import io
img_byte_array = io.BytesIO()
img.save(img_byte_array, format='PNG')

# Convert to base64
import codecs
base64_img_text = codecs.encode(img_byte_array.getvalue(), 'base64')

# Turn in to an HTML img tag with data embedded
html_img_tag = "<img src=\"data:image/png;base64, %s\" />" % codecs.decode(base64_img_text, 'ascii')
print(html_img_tag)
