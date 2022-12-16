fname = input("Enter file name: ")
fhand = open(fname)
for lx in fhand :
    ly = lx.rstrip()
    print(ly.upper())
