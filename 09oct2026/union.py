s =set()
l =[1,2,3,3,2,1]
s.update(l)
m = set([1,2,1,3,7])
print(s.union(m))
print(s.intersection(m))
print(m-s)