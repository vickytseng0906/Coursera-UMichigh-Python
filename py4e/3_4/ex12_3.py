import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
position = input('Enter position: ')

# Retrieve all of the anchor tags
_count = 0
_position = 0
while _count < int(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        _position = _position + 1
        if _position == int(position):
            url = tag.get('href', None)
            print(url)
            _position = 0
            _count = _count + 1
            break
