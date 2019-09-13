# Run with
# FLASK_APP=simple.py python -m flask run

# or directly with
# python simply.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'It works'



if __name__ == '__main__':
    app.run()