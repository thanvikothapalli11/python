#set
#collection of elements

s={}
print(s)
print(type(s))

l=[1,2,3,4,5]
s=set(l)
print(s)

# s={1,2,3,4,5}
# print(s[1:5])

s1={1,2,3,4,5}
s2={5,6,7,8}
print(s1.union(s2))

print(s1.intersection(s2))
print(s1.difference(s2))