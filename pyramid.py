n=int(input("length:"))
a=int(n/2)+1
for i in range(1,a+1):
    for j in range(a+1,i,-1):
        print("  ",end="")
    for k in range(1,i*2):
        print("* ",end="")
    print("")
        
