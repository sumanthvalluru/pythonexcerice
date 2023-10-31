'''s={1,2,3,4,5,6,7,8,9,7,6,5,4,3,2,2,1}
print(s)
s.add(32)
print(s)
s.update({6,8,96,97,8,})
print(s)
s.pop()
print(s)
s.remove(4)
print(s)
for i in s:
    print(i)'''
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))