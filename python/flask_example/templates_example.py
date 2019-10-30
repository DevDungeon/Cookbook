from flask import Flask, render_template, make_response

app = Flask(__name__, template_folder='templates')

@app.route('/page1')
def page1():
    # Simple template rendering
    # Returns `templates/some_template.html`
    return render_template('some_template.html')

@app.route('/page2')
def page2():
    # To pass arguments, use keyword arguments
    # Example template contents:
    """
    <html><body>
     <h1>{{ greeting }}</h1
    """
    return render_template('mypage.html', greeting='Hello')

@app.route('/page3')
def page3():
    # Return a 403 status code with error page
    # by using `make_response()`
    return make_response(render_template('forbidden.html'), 403)


if __name__ == '__main__':
    app.run()