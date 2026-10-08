a =input()
li =[]
for c in a:
    if c not in li:
        li.append(c)
ma =list(map(ord,li))
print(sum(ma))       
