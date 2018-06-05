import os
from flask import Flask, render_template
from picamera import PiCamera

BASE_DIR = '/home/pi/pycammy'
# Default static files dir: static/
# Default templates dir: templates/
app = Flask(__name__)

camera = PiCamera()
# camera.resolution = (2592, 1944)  # Max 2592x1944, Default: monitor size
# camera.brightness = 50  # 0-100, Default: 50

# You can use camera.image_effect to apply a particular image effect. 
# The options are: 
# none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch, gpen,
# pastel, watercolor, film, blur, saturation, colorswap, washedout, posterise,
# colorpoint, colorbalance, cartoon, deinterlace1, and deinterlace2. The default is none.

@app.route('/')
def index():
    # camera.annotate_text = "Hello world!" # date
    # camera.annotate_foreground = Color('yellow')
    image_url = '/static/image.jpg'
    camera.capture(BASE_DIR + image_url)
    return render_template('index.html', image_url=image_url)
    #return '<a href="/images/image.jpg">Image</a>'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, ssl_context=('cert.pem', 'key.pem'))
