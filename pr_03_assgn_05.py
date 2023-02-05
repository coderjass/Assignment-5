side1=float(input('Enter the length of 1st side: '))
side2=float(input('Enter the length of 2nd side: '))
side3=float(input('Enter the length of 3rd side: '))
if side1+side2<side3 or side1+side3<side2 or side2+side3<side1: 
    print("Error: Triangle can't be formed")
else:
    s=(side1+side2+side3)/2
    import math
    area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    print('Area of triangle is ', area)

    