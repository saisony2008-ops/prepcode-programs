l =[]
n =int(input())
for i in range(n):
    a =int(input())
    l.append(a)
l =sorted(l)
l =l[::-1]
c =l.count(max(l))
print(l[c])    
