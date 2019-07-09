import urllib
from bs4 import BeautifulSoup

url = input("Enter URL:")
count = int(input("Enter count:"))
position = int(input("Enter position:"))
print (url)
for i in range(1,count+1):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    url = tags[position-1].get('href')
    print(url)
