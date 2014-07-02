# Example

```python
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response(
        '200 OK',
        [('Content-Type', 'text/plain')]
    )
    return ['Hello, WSGI\n']


if __name__ == '__main__':
    server = make_server('', 8000, application)
    server.serve_forever()
```
