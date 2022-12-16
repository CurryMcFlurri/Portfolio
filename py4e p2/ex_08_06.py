lst = list()
while True:
    num = input('Enter a number: ')
    if num == 'done' :
        break
    try:
        inum = int(num)
        lst.append(inum)
    except:
        print('Invalid input')
        continue
print(lst)
print('Maximum is', max(lst))
print('Minimum is', min(lst))
