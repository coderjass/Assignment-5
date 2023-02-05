rows=int(input('Enter the number of rows: '))
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets_new=alphabets*99999999
i=0
j=1
z=1
for line in range(0,rows):
    print(alphabets_new[i:j])
    i=j
    z=z+1
    j=j+z
    
    

