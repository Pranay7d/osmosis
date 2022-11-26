import math

print('''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponent/Power
7. Square Root
8. Sin
9. Cos
10.Tangent
11.Radain to Degree
12.Degree to Radian

''')
inp=int(input("Enter the choise: "))
if inp>=1 and inp<=6:
    if inp == 1:
        first=float(input("enter the first number: "))
        second=float(input("enter the second number: "))
        print(first+second)
    elif inp ==2:
        first=float(input("enter the first number: "))
        second=float(input("enter the second number: "))
        print(first-second)
    elif inp ==3:
        first=float(input("enter the first number: "))
        second=float(input("enter the second number: "))
        print(first*second)
    elif inp ==4:
        first=float(input("enter the first number: "))
        second=float(input("enter the second number: "))
        print(first/second)
    elif inp ==5:
        first=float(input("enter the first number: "))
        second=float(input("enter the second number: "))
        print(first**second)
    elif inp==6:
        first=float(input("enter the first number: "))
        second=float(input("enter the second number: "))
        print(first%second)
elif inp>=7 and inp<=12:
    if inp==7:
        first=float(input("enter the number: "))
        print(math.sqrt(first))
    elif inp==8:
        first=float(input("enter the number: "))
        print(math.sin(first))
    elif inp==9:
        first=float(input("enter the number: "))
        print(math.cos(first))
    elif inp==10:
        first=float(input("enter the number: "))
        print(math.tan(first))
    elif inp==11:
        first=float(input("enter the value in Radian: "))
        print(numpy.degrees(first))
    elif inp==12:
        first=float(input("enter the value in Radian: "))
        print(numpy.radians(first))
else:
    print("invalid")
while True:
    choise=input('Do you want to contnue (y/n)? ')
    if choise=='y':
        inp=int(input("Enter the choise: "))
        if inp>=1 and inp<=6:
            if inp == 1:
                first=float(input("enter the first number: "))
                second=float(input("enter the second number: "))
                print(first+second)
            elif inp ==2:
                first=float(input("enter the first number: "))
                second=float(input("enter the second number: "))
                print(first-second)
            elif inp ==3:
                first=float(input("enter the first number: "))
                second=float(input("enter the second number: "))
                print(first*second)
            elif inp ==4:
                first=float(input("enter the first number: "))
                second=float(input("enter the second number: "))
                print(first/second)
            elif inp ==5:
                first=float(input("enter the first number: "))
                second=float(input("enter the second number: "))
                print(first**second)
            elif inp==6:
                first=float(input("enter the first number: "))
                second=float(input("enter the second number: "))
                print(first%second)
        elif inp>=7 and inp<=12:
            if inp==7:
                first=float(input("enter the number: "))
                print(math.sqrt(first))
            elif inp==8:
                first=float(input("enter the number: "))
                print(math.sin(first))
            elif inp==9:
                first=float(input("enter the number: "))
                print(math.cos(first))
            elif inp==10:
                first=float(input("enter the number: "))
                print(math.tan(first))
            elif inp==11:
                first=float(input("enter the value in Radian: "))
                print(numpy.degrees(first))
            elif inp==12:
                first=float(input("enter the value in Radian: "))
                print(numpy.radians(first))
        else:
            print("invalid")
    elif choise=='n':
        print("Thankyou for using")
        break