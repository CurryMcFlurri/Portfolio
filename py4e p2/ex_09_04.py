name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
counts = dict()
fh = open(name)
for lines in fh:
    #print(lines.strip())
    if not lines.startswith('From '): continue
    words = lines.split()
    #print(words)
    addresses = words[1]
    #print(addresses)
    #print(type(addresses))
    counts[addresses] = counts.get(addresses, 0) + 1
print(counts)
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
