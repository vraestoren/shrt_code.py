# <img src="https://camo.githubusercontent.com/3f02cb5f82b58be4f364387941dab57cd9146c0c2f9ed2f87c4c0e880c3b4bdf/68747470733a2f2f696d616765732d6170696c6973742d66756e2e73666f322e63646e2e6469676974616c6f6365616e7370616365732e636f6d2f73687274636f2e64655f6170695f6170692e706e67" width="50" style="vertical-align:middle;" /> shrtcode.py
> Web-API for the [shrtco.de](https://shrtco.de) URL Shortener API = shorten, protect, customize and inspect links with a simple interface.

---

## Usage

```python
from shrtcode import ShrtCode

client = ShrtCode()
result = client.shorten_url("https://example.com/very/long/link")
print(result["result"]["full_short_link"])
```

---

## Methods

| Method | Description |
|--------|-------------|
| `shorten_url(url)` | Shorten a URL |
| `protect_url(url, password)` | Shorten a URL with password protection |
| `generate_emoji_url(url)` | Get an emoji-based short link |
| `generate_custom_url(url, custom_code)` | Shorten with a custom short code |
| `get_url_information(code)` | Get info about a short link by its code |
| `get_status()` | Check the API status |
