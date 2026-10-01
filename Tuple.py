t=(10,)
print(t)
print(type(t))

t1=(10,20,30,'python','true')
print(t1[1])
print(t1[::-1])

t2=(10,20,30,40)
print(min(t2))
print(max(t2))

t3=('python','react','swift')
print(t3)
print(min(t3))
print(max(t3))

t4=(2,3,4,5,6,7,8)
len(t4)
print(len(t4))

t5=(10,20,30,40)
t5.index(30)
print(t5.index(30))

t6=(2,3,4,5,6,7,8,9,2,2)
t6.count(2)
print(t6.count(2))

#concatenation

x=(1,2,3,4)
y=(5,6,7,8)
print(x+y)

#repetition

x=(1,2,3,4)
y=4
print(x*y)

#membership

t7=(40,50,10,30,90)
t8=(tuple(sorted(t7)))
print(t8)
