d = {"admin":"cfokp345"}
log = {"admin":0}
old = {"admin":["admin123"]}
un = " "

def encryption(s):
    st=list(s)
    for i in range(0,len(st),1):
        c=ord(st[i])
        c+=2
        if(c>122):
            co=c-122
            c=97+co+1-2
        st[i]=chr(c)
    s1=''.join(map(str,st))
    return s1

def decrypt(s):
    st=list(s)
    for i in range(0,len(st),1):
        c=ord(st[i])
        c-=2
        if(c<97):
            co=97-c
            c=122-co+1
        st[i]=chr(c)
    s2=''.join(map(str,st))
    return s2

def storepass(pas):
    l=old[un]
    if(len(l)>=5):
        l.pop(0)
    if(pas in l):
        print("Password already used before, try new !!!")
        return False
    else:
        l.append(pas)
        print(l)
        old[un]=l
        return True

def changepwd():
    pwd = input("Enter new Password : ")
    if storepass(pwd):
        d[un] = encryption(pwd)
        print("Changed Successfully")
    else:
        print("miserably failed")

def auth(usr, pwd):
    pwd = encryption(pwd)
    if usr not in d:
        return False
    elif d[usr]==pwd:
        global un 
        un = usr
        if log[usr]>=5:
            print("You are using this password for a long time, pls change it")
            changepwd()
            log[usr] = 0
        else:
            return True
    else:
        return False

def login():
    print("**** User Interface ****")
    print()
    usr = input("Enter Username : ")
    pwd = input("Enter Password : ")
    if auth(usr, pwd):
        log[un] += 1
        print("Login Successfull !!!")
        return True
    else:
        print("Login Failed")
        return False
        
def register():
    print("**** Registrartion Interface ****")
    print()
    usr = input("Enter Username : ")
    pwd = input("Enter Password : ")
    cpd = input("Confirm Password : ")
    if pwd != cpd:
        print("confirm password and password didn't match")
    else:
        if usr not in d:
            d[usr] = encryption(pwd)
            log[usr] = 0
            old[usr] = [pwd]
            print("Successfully Registered !!!")
        else:
            print("User already exist")

# M A I N
print("**** HOMEPAGE Interface ****")
while(True):
    print()
    print("Press (1) for register\nPress (2) for login\nPress (3) for EXIT\n")
    opt = int(input("Enter option = "))
    if opt == 1:
        register()
    elif opt == 2:
        if login():
            print("Connection made")
            while(True):
                print("Press (1) to change password\nPress (2) to exit\n")
                oo = int(input("Enter option : "))
                if oo==1:
                    changepwd()
                else:
                    break
        else:
            print("Connection not made")
    elif opt == 3:
        print("Exited Successfully !!!")
        break
    else:
        print("Give correct input")
