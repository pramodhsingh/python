import os
os.system("cls||clear")

a=int(input("Compare numbers smaller or greater.\nA = "))
b=int(input("B = "))
c=int(input("C = "))

if ((a>b) and (a>c)):
    print("\n(A = %d) is greater than (B = %d) and (C = %d)" % (a,b,c))
elif (b>a) and (b>c):
    print("\n(B = %d) is greater than (A = %d) and (B = %d)" % (b,a,c))
elif (c>a) and (c>b):
    print("\n(C = %d) is greater than (A = %d) and (B = %d)" % (c,a,b))
elif (a==b) and a>c:
    print("\n(A = B = %d and greater than C = %d" % (a,c))
elif (a==c) and a>b:
    print("\n(A = C = %d and greater than B = %d" % (a,b))
elif (c==b) and c>a:
    print("\n(C = B = %d and greater than A = %d" % (c,a))
elif (a==b==c):
    print("\nAll the numbers are equlal\n\nA = B = C = %d" % a)