from urlparse import parse_qs
from urllib import quote
from wsgiref.simple_server import make_server


def get_url(environ):
    url = environ['wsgi.url_scheme'] + '://'

    if environ.get('HTTP_HOST'):
        url += environ['HTTP_HOST']
    else:
        url += environ['SERVER_NAME']

        if environ['wsgi.url_scheme'] == 'https':
          if environ['SERVER_PORT'] != '443':
              url += ':' + environ['SERVER_PORT']
        else:
          if environ['SERVER_PORT'] != '80':
               url += ':' + environ['SERVER_PORT']

    url += quote(environ.get('SCRIPT_NAME', ''))
    url += quote(environ.get('PATH_INFO', ''))
    if environ.get('QUERY_STRING'):
        url += '?' + environ['QUERY_STRING']
    return url


def application(environ, start_response):
    url = get_url(environ)
    query_string = parse_qs(environ['QUERY_STRING'])
    start_response(
        '200 OK',
        [('Content-Type', 'text/plain')]
    )
    return ['Hello, WSGI\n']


if __name__ == '__main__':
    server = make_server('', 8000, application)
    server.serve_forever()
