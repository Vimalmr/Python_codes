n=int(input("length:"))
a=int(n/2)+1

for i in range(1,a+1):
    for j in range(a+1,i,-1):
        print("  ",end="")
    for k in range(1,i*2):
        print("* ",end="")
    print("")

for i in range(a-1,0,-1):
    for j in range(i,a+1):
        print("  ",end="")
    for k in range((i*2)-1,0,-1):
        print("* ",end="")
    print("")
