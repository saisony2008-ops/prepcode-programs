l =[]
n =int(input())
for i in range(0,n):
    a =int(input("enter a"))
    l.append(a)
greatest =-1
for i in range(0,len(l)):
    if l[i]>greatest:
        greatest = l[i]
print(greatest)

