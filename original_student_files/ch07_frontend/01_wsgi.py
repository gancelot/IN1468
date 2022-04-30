from wsgiref.simple_server import make_server

hostname = 'localhost'
port = 8051


def application(environ, start_response):

    response_body = '<html><body><h1>Request received.</h1></body></html>'
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, headers)

    return [response_body.encode()]

httpd = make_server(hostname, port, application)
print(f'Server running on http://{hostname}:{port}...')
httpd.handle_request()                      # serves one request, localhost:8051
# httpd.serve_forever()                      # serves continuously
