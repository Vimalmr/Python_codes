n=int(input("Enter here:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* "*n);
    else:
        for j in range(n-i,0,-1):
            print("  ",end="")
        print("* ")
    
