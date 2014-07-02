# Example Explained

#### return value
http://legacy.python.org/dev/peps/pep-0333/#buffering-and-streaming

```python
def application(environ, start_response):
    return ['Hello', ', ', 'WSGI', '\n']
```

```python
def application(environ, start_response):
    yield 'Hello, '
    yield 'WSGI\n'
```
