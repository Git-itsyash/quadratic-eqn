import math

print("for quadratic equation,ax**2+bx+c=0,enter coefficients below")

a=int(input("enter a :"))
b=int(input("enter b :"))
c=int(input("enter a :"))

if a==0:
    print("value of",a,'should not be zero')
    print("\n Aborting !!!!!!")
else:
    delta=b*b-4*a*c
    if  delta>0:
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
        print("Roots are Real and Unequal")
        print("Root1=",root1,",Root2=",root2)
    elif delta==0:
        root1=-b/(2*a);
        print("Roots are Real and Equal")
        print("Root1=",root1,",Root2=",root1)
    else:
        print("Roots are Complex and Imaginary")
