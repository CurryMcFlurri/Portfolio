import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
trupos = pos - 1
repeats = 0
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Koddi.html"
print('Retrieving:', url)

while count > repeats:
    repeats = repeats + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    atag = tags[trupos]
    #print(atag)
    newurl = atag.get('href', None)
    print('Retrieving:', newurl)
    url = newurl
