sony =dict()
s =input("enter your name")
i = 0
for ch in s:
    if ch not in sony:
        sony[ch] =[i]
    else:
    sony[ch].append(i)
    i=i+1        
print(sony)        