a =input()
for row in range(a):
    for col in range(a):
        if col==0:
            print("*",end =" ")
        elif col==4:
            print("*",end =" ")
        elif row==3 or col==2:
            print("*",end =" ")
        elif row==4 or (row ==1 or col ==3):
            print("*",end =" ")    
        else:
            print(" ",end =" ")    
                    