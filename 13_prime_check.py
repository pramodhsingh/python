import os
os.system("cls||clear")

num = int(input("Enter a number to check prime: ")) 
flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print("\n",num, "is not a prime number")
else:
    print("\n",num, "is a prime number")