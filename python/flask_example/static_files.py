from flask import Flask, url_for

app = Flask(__name__, static_folder='public', static_url_path='/custom/path/')

@app.route('/')
def index():
    print(url_for('static',  filename='test.txt'))
    # Prints: /custom/path/test.txt
    # Maps to file: public/test.txt
    return 'Ok'


if __name__ == '__main__':
    app.run(debug=True)
