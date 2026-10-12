a =[1,2,3,4,160,200]
lis =set()
lis.update(a)
a = sorted(list(lis))
print(a)
seq =0
len =1
for i in range(l,lenght(a)):
    pre = cur-1
    if a[cur] == a[pre]+1:
        lenght =lenght+1
        seq =max(lenght,seq)
print(seq)        
    
