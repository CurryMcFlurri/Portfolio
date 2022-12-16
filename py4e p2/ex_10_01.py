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
# print using list comprehension
#print(sorted([(v, k) for k, v in counts.items()], reverse=True)[0])
#print(counts, '\n')
lst = list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)

for v, k in lst[:1]:
    print(k, v)
