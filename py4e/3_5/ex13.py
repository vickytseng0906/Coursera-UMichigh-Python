import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

data = urllib.request.urlopen(url).read()
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum = 0
for count in counts:
    print('count:', count)
    sum = sum + int(count.text)
    print('sum:', sum)
