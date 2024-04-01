a ={1,2,3,4,5}
a.add(6)
a.add("nepal")
print(a)
a.remove(5)
print(a)
b = a.copy()
b.clear()
print(b)


#difference
a = {'a','b','c','d','e'}
b = {'f','b','c','d','g'}
print(a.difference(b))
print(a.intersection(b))
print(a.isdisjoint(b))
print(a.issubset(b))


re =a.pop()
print(re)
y = {'a','b','c','d'}
rel =a.pop()
print(rel)
print(a.symmetric_difference(b))
print(a.union(b))