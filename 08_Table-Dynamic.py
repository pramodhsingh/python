import os
os.system('cls||clear')
a = int(input("***Print Table of a Number***\n\nEnter a Number: "))
b = int(input("Enter increment: "))

if (b==0 | b<a):
    print("\nInvalid Range, pleas try again...")

for a in range(a,b+1):
    for i in range(1,11):
        print(a, "x",i ,"=", a*i)
    print('\t')