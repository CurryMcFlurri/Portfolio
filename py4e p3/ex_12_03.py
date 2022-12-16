import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

#print(html)
#print(len(html))
#print(type(html))


if len(html) < 3000:
    print(html, '\n')
    print(len(html), 'characters retrieved.')
else:
    print(html[:3000], '\n')
    print('3000 characters displayed.')
    print(len(html), 'characters retrieved.' '\n')
