from wsgiref.simple_server import make_server

def application(environ, start_response):
    if environ['REQUEST_METHOD'] != 'POST':
        start_response('400 Bad Request', [
            ('Content-Type', 'text/plain'),
        ])
        return ['Only POST requests allowed']

    content_length = int(environ['CONTENT_LENGTH'])
    data = environ['wsgi.input'].read(content_length)
    start_response('200 Ok', [
        ('Content-Type', 'text/plain'),
    ])
    return [data]

if __name__ == '__main__':
    server = make_server('', 8000, application)
    server.serve_forever()
