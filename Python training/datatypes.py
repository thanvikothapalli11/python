# int , float , str , bool , list , tuple , set , dict.
a = 10
print(a)
print(type(a))
b = 2.5
print(b)
print(type(b))
c = 'asha'
print(c)
print(type(c))
d = True
print(d)
print(type(d))
e = [1,2,3]
print(e)
print(type(e))
f = (4,5,6)
print(f)
print(type(f))
g = {7,8,9}
print(g)
print(type(g))
h = {'name': 'luna' , 'age':'25' , 'city': 'korea'}
print(h)
print(type(h))

#string to int
#string to float
#int to string
#float to string
#int to list
#float to tuple
#list to tuple
x= 11
y= int(x)
print(y)
print(type(y))
x = '10'
y = float(x)
print(y)
print(type(y))
x= 6
y= str(x)
print(y)
print(type(y))
x= 20.5
y= str(x)
print(y)
print(type(y))
x= 77,55,66
y= list(x)
print(y)
print(type(y))
x= 11.7,2.5,3.1
y= tuple(x)
print(y)
print(type(y))
x= 1,2,3
y = tuple(x)
print(y)
print(type(y))

x = 'python'
result = list(x)
print(result)
num = (1,2,3)
result = list(num)
print(result)

A = [11,22,33]
result = tuple(A)
print(result)

import keyword
keywords = keyword.kwlist
print(keywords)
print(len(keywords))