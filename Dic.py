# S1={ 101:'Avinash',
#      102:'Srikhar',
#      103:'Kiran' }
# print(S1)
# print(S1.keys())
# print(S1.get(101))
# #print (S1.pop())
# print(S1.remove(103))

# d1=dict({100:'web',200:'java',300:'moon'})
# print(d1)
# d2=dict([(333,'lyra'),(666,'riga'),(777,'sun')])
# print(d2)
# d3=dict((('1','asha'),('2','light'),('3','rigel')))
# print(d3)


#len()
d=dict({100:'luna',200:'asha',300:'thanu'})
print(len(d))

#clear
d=dict({1:'moon',2:'sun',3:'earth'})
print(d.clear())

#get
d=dict({1:'kiwi',2:'lemon',3:'apple'})
d1={1:'kiwi',2:'lemon',3:'apple'}
print(d1[1])
print(d1.get(300))
print(d1.get(3))
print(d1.get(2,'lemon'))
print(d1.get(5,'lemon'))


#pop

# d={1:'kiwi',2:'lemon',3:'apple'}
# print(d.pop(2))
# print(d.pop(5))


#popitem
# d={1:'kiwi',2:'lemon',3:'apple'}
# print(d.popitem())
# d={}
# print(d.popitem())


#keys
d={1:'kiwi',2:'lemon',3:'apple'}
print(d.keys())
for k in d.keys():
    print(k)


#values
d={1:'kiwi',2:'lemon',3:'apple'}
print(d.values())
for k in d.values():
    print(k)

d={1:'kiwi',2:'lemon',3:'apple'}
print(d.items())
for k,v in d.items():
    print(k,'--->',v)

d={1:'kiwi',2:'lemon',3:'apple'}
t=d.copy()
print(id(d))
print(id(t))

#setdefault
d={1:'kiwi',2:'lemon',3:'apple'}
print(d.setdefault(1,'kiwi'))
print(d.setdefault(5,'mango'))


#update
d={1:'kiwi',2:'lemon',3:'apple'}
a={'t':'moon'}
d.update(a)
print(d)
d.update([(7,'S')])
print(d)
