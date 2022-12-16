import re

name = input('Enter File Name: ')
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
total = 0
count = 0
for line in fh:
    line = line.rstrip()
    digits = re.findall('New Revision: ([0-9]+)', line)
    if not len(digits) >= 1 : continue
    count = count + 1
    for numbers in digits:
        number = float(numbers)
        total = total + number
        avg = total/count
print(avg)
