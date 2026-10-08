a =input()
li =[]
for c in a:
    if c not in li:
        li.append(c)
tot =0
for val in li:
    tot =tot+ord(val)
print(tot)            
