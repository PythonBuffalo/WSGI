# Example Explained

#### environ
http://legacy.python.org/dev/peps/pep-0333/#environ-variables
```python
def application(environ, start_response):
    from pprint import pprint
    pprint(environ)
```
