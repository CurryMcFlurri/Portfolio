import re
name = input('Enter File Name: ')
if len(name) < 1:
    name = "regex_sum_1514005.txt"
fh = open(name)
total = 0
for line in fh:
    line = line.rstrip()
    digits = re.findall('[0-9]+', line)
    if not len(digits) >= 1 : continue
    for numbers in digits:
        number = int(numbers)
        total = total + number
print('Total: ', total)
