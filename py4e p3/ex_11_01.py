import re

input = input('Enter a regular expression:')
fh = open('mbox.txt')
count = 0
for line in fh:
    result = re.findall(input, line)
    if not len(result) >= 1: continue
    count = count + 1

print('mbox.txt had', count, 'lines that matched', input)
