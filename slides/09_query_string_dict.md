# Query String Dict

https://docs.python.org/2/library/urlparse.html#urlparse.parse_qs

```python
form urlparse import parse_qs

def application(environ, start_response):
    query_string = parse_qs(environ['QUERY_STRING'])
    print query_string
    return []
```

#### Result
`http://localhost:8000/?Key=Value`
```json
{'Key': ['Value']}
```
