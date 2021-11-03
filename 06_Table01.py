import os
os.system('cls||clear')
a = int(input("***Print Table of a Number***\n\nEnter a Number: "))
b = int(input("Enter increment: "))


for i in range(1,b+1):
    print(a, "x",i ,"=", a*i)