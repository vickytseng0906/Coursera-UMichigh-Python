import json
import urllib.request, urllib.parse, urllib.error

url = input ("Enter Location: ")
data = urllib.request.urlopen(url).read()
print('Retrieving', url)

sum = 0
#while True:
print('Retrieved', len(data), 'characters')
info = json.loads(data)
info = info['comments']
for item in info:
    sum += int(item['count'])
print('Sum:', sum)
    #break
