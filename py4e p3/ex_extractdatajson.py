import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst = list()
while True:
    url = input('Enter URL: ')
    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/comments_1514010.json"
    if url == 'done': break
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    info = json.loads(data)
    #print(json.dumps(info, indent=2))
    users = info["comments"]
    #print(users)
    for count in users:
        #print(count["count"])
        lst.append(count["count"])
        #print(lst)
    print(sum(lst))
