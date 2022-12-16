import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst = list()
url = input('Enter URL: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1514009.xml"
print('Retrieving:', url)
xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    #print(count.text)
    lst.append(float(count.text))
    #print(lst)
print('Count:', len(lst))
print('Sum:', sum(lst))
