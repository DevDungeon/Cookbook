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