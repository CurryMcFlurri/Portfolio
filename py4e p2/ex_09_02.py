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
    day = words[2]
    #print(addresses)
    #print(type(addresses))
    counts[day] = counts.get(day, 0) + 1
print(counts)
