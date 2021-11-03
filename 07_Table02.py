import os
os.system('cls||clear')
a = int(input("***Print Table of a Number***\n\nEnter a Number: "))
b = int(input("Enter increment: "))

print("\nTable using For Loop\n")
for i in range(1,b+1):
    print(a, "x",i ,"=", a*i, 
    "\t",a+1, "x",i ,"=", (a+1)*i, 
    "\t",a+2, "x",i ,"=", (a+2)*i, 
    "\t",a+3, "x",i ,"=", (a+3)*i,
    "\t",a+4, "x",i ,"=", (a+4)*i)
print("\n")