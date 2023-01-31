n=int(input("Enter here:"))
for i in range(1,n):
    for j in range(i):
        print("* ",end="")
    for k in range(n*2-2,i*2,-1):
        print("  ",end="")
    for j in range(i):
        print("* ",end="")
    print()
for i in range(n-2,0,-1):
    for j in range(i):
        print("* ",end="")
    for k in range(i*2+2,n*2):
        print("  ",end="")
    for j in range(i):
        print("* ",end="")
    print()
