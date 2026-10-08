l =list()
n =int(input())

for i in range(0,n):

    a =int(input("enter a"))
    l.append(a)
sum =0
for val in l:
    sum = sum+val
print(sum)    