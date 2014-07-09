# URL Reconstruction

http://legacy.python.org/dev/peps/pep-3333/#url-reconstruction

<small>
```python
from urllib import quote

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
```
</small>
