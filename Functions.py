# def sum(a,b,c):
#     result =a+b+c
#     print(result)
# sum(10,20,30) 
#           

# def area(r):
#     result=22/7
#     area=result*r*r
#     print(area)
# area(7)

# def square_number(x):
#     square_number=x*x
#     print(square_number)
# square_number(4)


# def shopping_bill(price,quantity):
#     result=price*quantity
#     print("your bill is:",result)
# shopping_bill(10,20)

# def check_even(num):
#     if num %2==0:
#           print("even")
#      else:
#          print("not even")
# n=int(input("enter a num:"))
# print(check_even(n))

# def add(a,b):
#     return a+b
# result=add(5,3)
# print(result)

'''----FUNCTIONS----'''
# Function:A group of line with some name is called function.
# A group of functions saved in one file is called module.
# A group of modules is ntg but a package.
# A group of package is ntg but a library.


'''---Types of arguments'''
'''-------Positional arg-------'''
# def greet(name,wish):
#     print("hello",name,wish)
# greet('avinash','good morning')
 
# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     result=sum,sub
#     print(result)
# sum_sub(100,500)
# sum_sub(500,100)

'''----Keyword arg-----'''
# def greet (name,wish):
#     print("hello",name,wish)
# greet(name="asha",
#     wish='good night')
# greet(wish='good night',name='asha')

# def greet(name,age,city):
#      print("hello",name ,age ,city)
# greet(name='thanvi',age='17',city='skht')

# def movie(hero,villian):
#     print("hello:",hero)
#     print("hello:",villian)
# movie(hero='nani',villian='gowtham raj')

'''----Default arg-----'''
# def greet(name='ravi',age=21):
#     print("hello",name,age)
# greet()

# def movie(hero='bob'):
#     print("hello",hero)
# movie()
# movie("pawan")
    

'''-----Variable Length-----'''

# def f2(n1,*s):
#     print(n1)  
#     print(*s)
# f2(10,'A',20,'B',30)

# def f3(*s,n2):
#     print(s)
#     print(n2)
# f3(10,'A',20,'B',30,'C',n2='C')


# def f(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
# f(3,2)
# f(10,20,30,40)
# f(25,50,arg4=100)
# f(arg4=2,arg1=3,arg2=4)
# f()
# f(4,5,arg2=6)
# f(arg3=10,arg4=20,30,40)
# f(4,5,arg3=5,arg5=6)

# def f1(**a):
#     print(a)
#     print(type(a))
# f1(a=10,b=20,c=30,d=40)

# Global variable

# a='This is global variable'
# b=10
# def g():
#     print(a)
#     print(b)

# def g1():
#         print(a)
#         print(b)
# g()
# g1()

#Local variable

# def l():
#     a='This is local variable'
#     b=10
#     print(a)
#     print(b)

# def l1():
#         print(a)
#         print(b)
# l()
# l1()

'''-----Lambda function------'''
# s=lambda n:n+n
# print(s(2))

# s=lambda x: "Even" if x % 2 == 0 else"Odd"

# print(s(1))
# print(s(4))


# greater = lambda x, y: x if x > y else y
# num1 = 10
# num2 = 25
# result = greater(num1, num2)

# print("The greater number is: {result}")  


'''----Recurrsive function-----'''

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(5))

# def is_palindrome(s):

#     if len(s) <= 1:
#         return True
    
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])
# print(is_palindrome("racecar"))  
# print(is_palindrome("python"))   
# print(is_palindrome("noon"))    