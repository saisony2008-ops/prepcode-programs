li =[]
n =int(input())
for i in range(n):
    a =int(input())
    li.append(a)
ans =[]
for val in li:
    if li.count(val)>1 and val not in ans:
        ans.append(val)
print(ans)            