l =[]
n =int(input("enter n:"))
for i in range(0,n):
    a =int(input("enter a"))
    l.append(a)
l.sort()
print("second greatest:",l[-2])    


