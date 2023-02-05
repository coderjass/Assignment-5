num=list()
for x in range(0,10):
    z=int(input('Enter number: '))
    num.append(z)
for a in num:
    if a>0:
        print(a, 'is a positive number')
    else:
        print(a, 'is a negative number')
    if a%2==0:
        print(a, 'is an even number')
    else:
        print(a, 'is an odd number')
    times=num.count(a)
    print(a, 'has occured', times, 'times in the given list')
    
