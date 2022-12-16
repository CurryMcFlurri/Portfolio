name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
counts = dict()
fh = open(name)
for lines in fh:
    #print(lines.strip())
    if not lines.startswith('From '): continue
    words = lines.split()
    #print(words, '\n')
    timestamp = words[5]
    #print(timestamp, '\n')
    #print(type(timestamp))
    pieces = timestamp.split(':')
    #print(pieces)
    hr = pieces[0]
    #print(hr)
    counts[hr] = counts.get(hr, 0) + 1
    #print(counts)
for k,v in sorted(counts.items()):
    print(k,v)
