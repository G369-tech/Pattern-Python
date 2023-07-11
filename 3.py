for i in range(1,15):
    for j in range(1,16):
        if j==1:
            if i==2 or i==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if j==2:
            if i==1 or i==7 or i==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if j==3:
            if i==1 or i==7 or i==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if j==4:
            if i==1 or i==7 or i==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if j==5:
            if i==2 or i==3 or i==5 or i==6:
                print("*",end="")
            else:
                print("",end="")
    print()
