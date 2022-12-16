fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for lines in fh:
    #print(lines.rstrip())
    words = lines.split()
    #print(words)
    for wrd in words:
        #print(wrd)
        if not wrd in lst:
            lst.append(wrd)
            #print(lst)
            #abclist=lst.sort()
lst.sort()
print(lst)
