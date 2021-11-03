import os
os.system("cls||clear")

num = int(input("Enter a Number to find factors: "))  

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

print_factors(num)