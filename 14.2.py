import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address})
print('Retrieving',url)
uh = urllib.request.urlopen(url,context=ctx)
data = uh.read().decode()
print('Retrieved',len(data),'charactors')
js = json.loads(data)
if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    exit()
Place_id = js["results"][0]['place_id']
print(Place_id)
