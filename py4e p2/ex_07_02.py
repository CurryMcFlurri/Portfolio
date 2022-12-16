# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if fname == 'na na boo boo':
    print('''NA NA BOO BOO TO YOU - You have been punk'd!''')
else:

    try:
        fh = open(fname)
        count = 0
        tot = 0
        for line in fh:
            if not line.startswith("X-DSPAM-Confidence:"): continue
            count = count + 1
            sppos = line.find(' ')
            #print(sppos)
            val = line[19:]
            #print(val)
            fval = float(val)
            #print(fval)
            tot = tot + fval
            #print(tot)
            avg = tot/count
            #print(avg)
        print('Average spam confidence:',tot/count)
    except:
        print('File does not exist')
