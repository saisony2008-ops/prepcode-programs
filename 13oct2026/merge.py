d1 ={'a':10,'b':20,'c':30}
d2 ={'a':40,'b':50,'c':60}
d =d1.copy()
for key in d2:
    if key in d:
        d[key]+=d2[key]
    else:
        d[key]=d2[key]  
print(d)          