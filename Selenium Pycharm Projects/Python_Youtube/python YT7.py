# class myclass:
#     def func(self):
#         pass
#     def display(self,name):
#         print(name)
# mc1=myclass()
# mc1.func()
# mc1.display("scott")
#----------------------------------------
# class myclass:
#     def m1(self):
#         print("Instance method")
#     def m2(self,number):
#         print(self,number)
# obj=myclass()
# obj.m1()   #instance method we can invoke/call through object
# obj.m2(10,20)    #ERROR bcoz m2 method expects only two arguments: self (implicitly passed) and number. When you call obj.m2(10, 20), you're providing two arguments explicitly, but the method signature only accepts one (number). The self parameter is automatically provided when calling via an instance, so m2 is actually receiving three arguments: self, 10, and 20, which results in a TypeError.

#----------------------------------------
# class myclass:
#     def m1(self,a):
#         print("Instance method",self,a)
#     def m2(self,number1,number2):
#         print(self,number1,number2)
# obj=myclass()
# obj.m1(30)   #instance method we can invoke/call through object
# obj.m2(10,20)    #instance method we can invoke/call through object

#----------------------------------------
# class myclass:
#     def m1(self,a):
#         print("Instance method",self,a)
#     @staticmethod
#     def m2(self,number1,number2):
#         print("static method", self,number1,number2)
# obj=myclass()
# obj.m1(40)   #instance method we can invoke/call through object
# myclass.m2(10,20,30)    #instance method we can invoke/call through object
#----------------------------------------

# c=30    # Global variable
# class myclass:
#     a,b=10,20   #class variables
#     def add(self):
#         print(self.a+self.b+self.c)   #ERROR since c is a global variable, it should be accessed directly without the self prefix.
#     def multi(self):
#         print(self.a*self.b)
#     def sub(self):
#         print(self.a-self.b)
# mc=myclass()
# mc.add()
# mc.multi()
# mc.sub()
#----------------------------------------

# c = 30  # Global variable
# class MyClass:
#     a, b = 10, 20  # Class variables
#
#     def add(self):
#         print(self.a + self.b + c)  # Access global variable `c` directly
#
#     def multi(self):
#         print(self.a * self.b)
#
#     def sub(self):
#         print(self.a - self.b)
#
# mc = MyClass()
# mc.add()    # Output: 60 (10 + 20 + 30)
# mc.multi()  # Output: 200 (10 * 20)
# mc.sub()    # Output: -10 (10 - 20)

#----------------------------------------
# i,j,k=10,20,30  #global variables

# class myclass:
#     a,b=40,50   #Class Variable
#     def add(self, x, y):    # x & y are local variables
#         print(x+y)  # x & y are local variables
#         print(self.a+self.b)    # a & b are class variable
#         print(i+j+k)  # i , j & K are global variables
#
# obj=myclass()
# obj.add(100,200)
#----------------------------------------
# a,b=15,25
# class myclass:
#     a,b=10,20
#     def add(self,a,b):
#         print(a+b)  #local variable
#         print(self.a+self.b)    #class variable
#         print(globals()['a']+globals()['b'] )   #Global variable
# mc=myclass()
# mc.add(100,200)

#----------------------------------------

# a, b = 15, 25  # Global variables
# class MyClass:
#     a, b = 10, 20  # Class variables
#     @staticmethod
#     def add(a, b):  # Local variables (arguments)
#         print(a + b)  # This will print the sum of the local variables `a` and `b`
#
#         # To access class variables within a static method, use the class name:
#         print(MyClass.a + MyClass.b)  # This will print the sum of the class variables `a` and `b`
#
#         # Accessing global variables
#         print(a+b)  # This will print the sum of the global variables `a` and `b`
#
#
# mc = MyClass()
# MyClass.add(100, 200)

#----------------------------------------
                                #multiple object in one class
# class myclass:
#     def display(self,name):
#         print("this is display method")
#         print(name)
#
# obj=myclass()
# obj.display("john")
#
# obj1=myclass()
# obj1.display("scott")
#----------------------------------------
                                #Constructor
#constructor will not return the value
#constructor can also take arguments / parameters
#constructor will be called at the time of object creation

# class myclass:
#     def __init__(self):               #constructor will not return the value
#         print("this is a constructor")
#     def m1(self):
#         print("hello....")
#     def m2(self,x,y):
#         return(x+y)
# mc=myclass()
# mc.m1()
# print(mc.m2(10,20))
#----------------------------------------
# class myclass:
#     fnames="john"
#     def __init__(self,lname):        #contructor expecting one argument
#         print(myclass.fnames)
#         print(lname)
#
# obj=myclass("ahmed")        #passing parameter to the contructor
#----------------------------------------
# class Emp:
#     def __init__(self, e_id, e_name, salary):  # e_id, e_name, salary are local variables here
#         self.e_id1 = e_id  # self.e_id is an instance variable
#         self.e_name1 = e_name  # self.e_name is an instance variable
#         self.salary1 = salary  # self.salary is an instance variable
#
#
#     def display(self):
#         print(self.e_id1, self.e_name1, self.salary1)  # Accessing instance variables
#
# # Creating the first object
# obj = Emp(101, 'John', 500000)  # e_id=101, e_name='John', salary=500000 are local in this context
# obj.display()   # This accesses the instance variables and prints: 101 John 500000
#
# # Creating the second object
# obj1 = Emp(102, 'Scott', 700000)    # e_id=101, e_name='John', salary=500000 are local in this context
# obj1.display()  # # This accesses the instance variables and prints: 102 Scott 700000
#----------------------------------------
# class emp:
#     def __init__(self,e_id,e_name,salary):
#         self.e_id=e_id
#         self.e_name=e_name
#         self.salary=salary
#     def __str__(self):      #this is another type of constructor which is string constructor.
#         return(self.e_name)     #it only accepts string variable 
#         return(self.e_name,self.salary) #INVALID bcoz __str__() returns only string data
# obj=emp(101,'john',500000)    
# print(obj)    













