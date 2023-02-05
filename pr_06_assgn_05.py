a=int(input('The range starts from: '))
b=int(input('Range ends to: '))
for prime in range(a,b+1):
    if prime>1:
        for num in range(2, prime):
             if prime%num==0:
                 break
        else:
            print(prime)
            
    

        