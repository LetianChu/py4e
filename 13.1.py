import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the location')
print('Retrieving',url)
mmp = urllib.request.urlopen(url,context=ctx)
# to read data
data = mmp.read()
print('Retrieved',len(data),'charactors')
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('Count:',len(lst))
ttl = 0
for item in lst:
    num = item.find('count').text
    num = int(num)
    ttl = ttl + num
print('Sum:',ttl)
