from flask import Flask

app = Flask(__name__)

# Simple route for all HTTP methods on landing page
@app.route('/')
def index():
    # Default response is HTML type
    return '<html><body>Ok</body></html>'

# Route only GET and POST methods
@app.route('/get-or-post', methods=['GET', 'POST'])
def get_or_post():
    return 'It works'


# Taking an variable in the URL path. Default type is `string`.
# Instead of `int` you can have: `float`, `path` or `uuid`
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    print("Id: %s" % product_id)
    return 'You requested product %s' % product_id

# Trailing slash makes a difference
# With test1, /test1 gets redirected to /test1/
# With test2, /test2/ comes up with no match.
@app.route('/test1/') # /test1 works, /test1/ works
@app.route('/test2')  # /test2 works, /test2/ fails
def trailing_slash():
    # Multiple routes can go to a single function
    return '<html><body>Works</body></html>'

def my_handler():
    return '<html><body>Ok</body></html>'

# You can also add routes without using the decorator,
# by calling `flask.Flask.add_url_rule()` like this:
app.add_url_rule('/the/url/', my_handler)


if __name__ == '__main__':
    app.run()
