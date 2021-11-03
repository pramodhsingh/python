import os
os.system("cls||clear")

print("\n***Print Fibonacci Series***")
n1, n2 = 0, 1
c0 = int (input("\nEnter the series range = "))
print()

print(n1,",", n2, end=", ")
for i in range(0,c0):
    b = n1 + n2
    print(b, end=", ")
    n1 = n2
    n2 = b
print()