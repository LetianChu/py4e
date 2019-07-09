import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter the location')
print('Retrieving',address)
url = urllib.request.urlopen(address,context=ctx)
data =  url.read().decode()
print('Retrieved',len(data),'charactors')
js = json.loads(data)
comments = js['comments']
ttl = 0
for item in comments:
    ttl = ttl + int(item['count'])
print('Sum:',ttl)
