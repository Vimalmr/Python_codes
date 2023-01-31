n=int(input("Enter here:"))

for i in range(1,n+1):
    for j in range(n,i,-1):
        print("  ",end="")
    print("* "*i)

for i in range(n-1,0,-1):
    for j in range(i,n):
        print("  ",end="")
    print("* "*i)
