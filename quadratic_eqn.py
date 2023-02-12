import math
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
c=int(input('Enter the value of c:'))
D=(b*b)-(4*a*c)
if D==0:
    root=(-b/(2*a))
    print('r1=r2=',root)
if D<0:
    print('Roots is imaginary')
if D>0:
    r1=(-b+math.sqrt(D))/(2*a)
    r2=(-b-math.sqrt(D))/(2*a)
    print('Root1=',r1)
    print('Root2=',r2)

