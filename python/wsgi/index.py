"""
Very simple WSGI python file example. point WSGIScriptalias here
"""

def wsgi_app(environ, start_response):
    output = "<html><body><h1>WSGI working!</ht></body></html>\n".encode('utf-8')
    status = '200 OK'
    headers = [('Content-type', 'text/html'),
               ('Content-Length', str(len(output)))]
    start_response(status, headers)
    yield output


# mod_wsgi needs the "application" variable to serve our small app
application = wsgi_app

# or Run with waitress
# python -m pip install waitress
# python -m waitress index:wsgi_app

if __name__ == '__main__':
    # Standard librar wsgi server
    import sys
    from wsgiref.simple_server import make_server
    print("Setting up server on 0.0.0.0:9999")
    try:
        make_server('0.0.0.0', 9999, wsgi_app).serve_forever()
    except KeyboardInterrupt:
        print('Exiting.')
        sys.exit(0)