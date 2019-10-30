from flask import Flask, url_for

app = Flask(__name__) # static_folder=None to disable

# Static files are served from `static/` and URL of `/static/`

if __name__ == '__main__':
    app.run()
