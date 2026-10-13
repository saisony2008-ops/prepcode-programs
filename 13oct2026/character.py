d ={}
s =input("enter the string ")
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1   
print(d)         