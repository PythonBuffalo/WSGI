import os.path
from wsgiref.simple_server import make_server


ROOT_DIR = os.path.abspath('./public')

def application(environ, start_response):
    url = environ['PATH_INFO']
    if os.path.isfile(ROOT_DIR + url):
        start_response('200 Ok', [
            ('Content-Type', 'text/plain'),
        ])
        fp = open(ROOT_DIR + url, 'r')
        if 'wsgi.file_wrapper' in environ:
            return environ['wsgi.file_wrapper'](fp, 1024)
        else:
            return iter(lambda: fp.read(1024), '')
    else:
        start_response('404 Not Found', [
            ('Content-Type', 'text/plain'),
        ]);
        return ['Not Found']


if __name__ == '__main__':
    server = make_server('', 8000, application)
    server.serve_forever()
