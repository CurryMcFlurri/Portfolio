fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
emails = list()
for lines in fh:
    lines=lines.rstrip()
    if not lines.startswith('From ') : continue
    words=lines.split()
    count=count+1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
