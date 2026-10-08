n = int(input())
for i in range(n):
    if i==0 or i==n//2 or i==n-1:
        print("*" *5)
    elif i<n//2:
        print("*")
    else:
         print("    *")



