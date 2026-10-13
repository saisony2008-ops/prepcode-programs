sony=dict()
s=input("enter your name")
for ch in s:
    if ch not in sony:
        sony[ch]=1
    else:
        sony[ch]=sony[ch]+1
print()            