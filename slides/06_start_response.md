# Example Explained

#### start_response
http://legacy.python.org/dev/peps/pep-0333/#the-start-response-callable

```python
start_response(status, response_headers, exc_info=None)
```

#### status
http://www.faqs.org/rfcs/rfc2616.html
```text
"200 Ok"
```

#### response_headers
http://www.faqs.org/rfcs/rfc2616.html
```python
[("Key", "Value"), ...]
```
