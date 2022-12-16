import string

name = input("Enter file:")
if len(name) < 1:
    name = "romeo.txt"
dictionary_counts = dict()
lst = list()
count = 0

try:
    fh = open(name)
except FileNotFoundError:
    print('File not found: ', fh)
    exit()

for lines in fh:
    lines = lines.translate(str.maketrans('', '', string.digits))
    lines = lines.translate(str.maketrans('', '', string.punctuation))
    lines = lines.lower()

    words = lines.split()
    #print(words)
    for word in words:
        for letter in word:
            count = count + 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1
print(dictionary_counts, '\n')

for k, v in list(dictionary_counts.items()):
    newtup = (v/count, k)
    lst.append(newtup)
    #lst.append((v / count, k))     #alternate way to append tuple to list
lst.sort(reverse=True)
#print(lst)
for key, val in lst:
    print(key, val)
