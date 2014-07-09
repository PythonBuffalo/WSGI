# Reading POST Data

http://legacy.python.org/dev/peps/pep-3333/#environ-variables
http://webpython.codepoint.net/wsgi_request_parsing_post

```python
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
```
