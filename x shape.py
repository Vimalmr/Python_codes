n=int(input("length:"))
a=int(n/2)+1
for i in range(1,n+1):
    if(i<=a):
        for k in range(1,i):
            print("  ",end="")
        for j in range(i,n+1):
            if(j==i or j==n-i+1):
                print("* ",end="")
            else:
                print("  ",end="")
        print("")
    else:
        for k in range(i,n-1):
            print("  ",end="")
        for j in range(1,n+1):
            if(j==i or j==n-i+1):
                print("* ",end="")
            else:
                print("  ",end="")
        print("")
