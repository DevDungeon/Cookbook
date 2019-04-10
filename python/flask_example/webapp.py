# http://flask.pocoo.org/docs/1.0/quickstart/
# python -m pip install flask

# Linux
# export FLASK_APP=webapp.py
# Windows command prompt
# set FLASK_APP=webapp.py
# PowerShell
# $env:FLASK_APP = "hello.py"

# Debug mode
# FLASK_ENV=development

# Run server
# flask run
# python -m flask run

# other flask commands
#  routes  Show the routes for the app.
#  run     Runs a development server.
#  shell   Runs a shell in the app context.

## Running server
#------------------
# Built in runner
# FLASK_APP=webapp.py python -m flask run

# Or Using the app object's .run() method from inside the script
# app.run()

## Or using standard library wsgiref
# from wsgiref.simple_server import make_server
# make_server('0.0.0.0', 9999, app).serve_forever()

## Or more production worthy wsgi server: waitress
# python -m pip install waitress
# python -m waitress webapp:app  # module name, class name




from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/<int:id>/<name>/<path:rest_of_path>', methods=['GET', 'POST'])
def hello(id, name, rest_of_path):
    if request.method == 'POST':
        return 'Posted.'
    response = make_response(render_template('page.html', data={'number': 25}))
    return response

if __name__ == '__main__':
    # Equivalent to ``FLASK_APP=webapp.py python -m flask run``
    app.run()



# HTTP Methods
#--------------
# @app.route('/', methods=['GET', 'POST'])
# if request.method == 'POST'


# # Route variables
# -----------------
# @app.route('/user/<username>') # string param
# def show_user_profile(username):

# @app.route('/post/<int:post_id>')  # param as int
# def show_post(post_id):

# @app.route('/path/<path:subpath>')  # full subpath with slashes
# def show_subpath(subpath):

# Variable types:
# -----------------
# string	(default) accepts any text without a slash
# int	accepts positive integers
# float	accepts positive floating point values
# path	like string but also accepts slashes
# uuid	accepts UUID strings


# Create urls for functions
#--------------------------
# from flask import url_for
# url_for('hello')  # Creates full url for "/" 
# print(url_for('login_funcname', next='/'))  #  /login?next=/
# print(url_for('profile_funcname', username='John Doe'))  # /user/John%20Doe

# Static files
#-----------------
# url_for('static', filename='main.js')
# # File is expected to live in ./static/main.js
# # Will be accessible at http://localhost/static/main.js


# Templates (jinja2 by default)
# ------------------------------
# # Expects templates in templates/ dir
# # Expects params as named arguments
# from flask import render_template
# return render_template('page.html', data=data)


# Access request info
#---
# from flask import request
# @app.route('/')
# def landing_page():
#   print(request.path)
#   print(request.method)
#   print(request.form['username'])  # Get POST data, raises KeyError
#   print(request.args.get('search_query', ''))  # Get GET data ?search_query=hello

# Modify response
#-----
# response = make_response(render_template('page.html'))
# response.headers['X-Custom'] = 'L33t!'
# return response

# Uploading files
# ------------------------ http://werkzeug.pocoo.org/docs/0.14/utils/#werkzeug.utils.secure_filename
# File is available in: f =  requests.files['file_name']
# You can save it: f.save('/path/to/save.txt')
# Use <form enctype="multipart/form-data" method="POST">
# Also available on the file object: f.filename (original filename), f.name (form field name), f.headers, f.close(), f.mimetype, f.mimetype_params
# Secure filename:
# from werkzeug.utils import secure_filename
# secure_filename(f.filename)

# Cookies
# request.cookies.get('username')
# response = flask.make_response(render_template('page.html'))
# response.set_cookie('key', 'value')
# return response

# Redirect
# return flask.redirect('/', code=302)

# Returning errors
# flask.abort(404)  # Immediate returns a response(throws exception)
# flask.abort(Response('sorry.'))

# Sending files back
# flask.send_file(filename_or_fp, mimetype=None, as_attachment=False, attachment_filename=None, add_etags=True, cache_timeout=None, conditional=False, last_modified=None)
# flask.send_from_directory('/path/to/uploads', 'file.txt')

# Configuration
# FLASK_ENV -> print(flask.config['ENV'])  # Default 'production'
# DEBUG
# TESTING
# SECRET_KEY
# SESSION_COOKIE_NAME
# SESSION_COOKIE_DOMAIN # Defaults to SERVER_NAME
# SERVER_NAME
# SESSION_COOKIE_SECURE
# SESSION_COOKIE_SAMESITE
# SESSION_COOKIE_HTTPONLY
# Production web server 
# gunicorn/waitress/apache mod wsgi/uwsgi

# Sessions http://flask.pocoo.org/docs/1.0/quickstart/#sessions


# Streaming data back
# Does not require a ton of memory to pass back something large (or infinite)
# from flask import Response

# @app.route('/large.csv')
# def generate_large_csv():
#     def generate():
#         for row in iter_all_rows():
#             yield ','.join(row) + '\n'
#     return Response(generate(), mimetype='text/csv')