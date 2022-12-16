import socket
#import ssl
# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

if not url.startswith('http://'):
    url = 'http://' + url

pieces = url.split('/')
host = pieces[2]
print(host)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((host, 80))
    cmd = 'GET %s HTTP/1.0\r\n\r\n' %url
    cmd = cmd.encode()
except:
    print('Error: not a valid url')
    quit()

mysock.send(cmd)

#string initialization
x = ''
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    x= x + data.decode()
    #for letter in data:    # my first method for counting characters in 'data'.
        #count = count + 1  # now redundant.

mysock.close()

if len(x) < 3000:
    print(x, '\n')
else:
    print(x[:3000], '...\n')
    print('Only', len(x[:3000]), 'characters displayed.')

print(len(x), 'characters were retrieved.')
