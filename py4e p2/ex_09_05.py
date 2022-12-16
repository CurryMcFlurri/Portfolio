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
    pieces = addresses.split('@')
    domain = pieces[1]
    #print(domain)
    counts[domain] = counts.get(domain, 0) + 1
print(counts)
