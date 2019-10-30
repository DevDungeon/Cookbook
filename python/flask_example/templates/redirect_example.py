from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Base landing page (no redirection yet)
    return '<html><body>Ok</body></html>'

@app.route('/home')
def homepage():
    # Redirect `/home` to `/` with 301 status code
    return redirect('/', 301)

@app.route('/dashboard')
def dashboard():
    # Redirect `/dashboard` to the URL of the `homepage` function
    # This allows you to reference a function name
    # without needing to know its URL
    # `url_for()` also accepts arguments to pass to the route.
    return redirect(url_for('homepage'))

@app.route('/devdungeon')
def devdungeon():
    # Redirect to an external source
    return redirect('https://www.devdungeon.com')


if __name__ == '__main__':
    app.run()