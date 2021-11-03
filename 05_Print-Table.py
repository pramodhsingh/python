import os
os.system('cls||clear')
a = int(input("***Print Table of a Number***\n\nEnter a Number: "))

print("\nTable using For Loop")
for i in range(1,11):
    print(a, "x",i ,"=", a*i)

print("\nTable using While Loop\n")
j=1
while j<=10:
    print(a, "x",j ,"=", a*j)
    j+=1