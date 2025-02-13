                                    #FUNCTIONS
# def myfunc():
#     print("hello")
# myfunc()
#----------------------------------------------
# def myfunc(name):
#     print("hello",name)
# myfunc("smith")
#----------------------------------------------
# def cal(a,b):
#     return (a+b)
# sum= cal(10,20)
# print(sum)
#----------------------------------------------
# def cal(a,b):
#     return (a+b)
# print(cal(10,20))
#----------------------------------------------
# def func():
#     return
# print(func())
#----------------------------------------------
# def func():
#     i=10   #not returning anything
# print(func())
#----------------------------------------------
# global_var=20
# def func():
#     local_Var=10
#     print(local_Var)
#     print(global_var)
# func()
#----------------------------------------------
# global_var=20
# def func():
#     local_Var=10
# func()
# print(global_var)
# print(local_Var)   #INVALID
#----------------------------------------------
# xy=100     #global variable
# def cool():
#     xy=200    #Local Variable
#     print(xy)
# cool()     #200
# print(xy)     #100
#----------------------------------------------
# xy=100     #global variable
# def cool():
#     global xy   #we use GLOBAL keyword to convert local into global keyword
#     xy=200    #Local Variable
#     print(xy)
# cool()     #200
# print(xy)
#----------------------------------------------
# x=100
# def cool():
#     global x
#     x=500
#     print(x)
# #cool()
# print(x)
#----------------------------------------------
# def cool():
#     global x
#     x=100
#     print(x)
# cool()
# print(x)   #able to access (x) bcoz it's a global variable.
#----------------------------------------------
                    #POSITIONAL ARGUMENTS
# def func(i,j):
#     print(i,j)
# func(10,20)    #POSITIONAL ARGUMENTS
#----------------------------------------------
                    #KEYWORD ARGUMENTS (order sequence is not important)
# def func(i,j):
#     print(i,j)
# func(j=10,i=20)    #KEYWORD ARGUMENTS(order sequence is not important)
#----------------------------------------------
                    #DEFAULT VALUES ASSIGNED TO POSITIONAL ARGUMENTS
# def func(i,j=10):
#     print(i,j)
# func(100,200)
# func(100)
#----------------------------------------------
                    #Keyword arguments(order sequence is not important)
# def greetings(name,greetmsg):
#     print(greetmsg+" "+ name)
# greetings(name='john', greetmsg='hello')   
# greetings(greetmsg='hello', name='john')
#---------------------------------------------- 
# def myfunc(a,b,c):
#     print(a,b,c)
# # myfunc(10,20,30)  #positional argument
# # myfunc(a=10,b=20,c=30)   #keyword argument
# # myfunc(b=20,a=10,c=30)   #keyword argument

# myfunc(10,20,c=30)
# myfunc(10,b=20,c=30)
# #myfunc(10,b=20,30)  #this is wrong, as positional argument must appear before any keyword argument. 
# #myfunc(10,30,b=20)   #this is having logical error, no order sequence. 
#---------------------------------------------- 
                #function can return multiple values
# def largest(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
# print(largest(10,20))
# print(largest(30,20))
# res=largest(10,20)
# print(res)
# print(type(res))













































