                                        #INHERITANCE
# Aquiring all the attributes (variables) & behavior (methods) from one class to another class is called inheritance.
# 4 Types of inheritance:
# single
# multi level
# heirarchy
# multiple
# ---------------------------------------------------
                                # SINGLE INHERITANCE
# class a:
#     def m1(self):
#         print("m1 method of class A")
# class b(a):
#     def m2(self):
#         print("m2 method of class B")
# obj=b()     #this is single inheritance
# obj.m1()
# obj.m2()
# ---------------------------------------------------
# class a:
#     x,y=10,20
#     def m1(self):
#         print(a.x,a.y)      #class variable called through class which is "a"
# class b(a):
#     a,b=100,200
#     def m2(self):
#         print(b.a-b.b)
#
# obj=b()
# obj.m1()
# obj.m2()
# ---------------------------------------------------
                                # MULTI LEVEL INHERITANCE
class a:
    x,y=10,20
    def m1(self):
        print(a.x+a.y)    #class variable called through class which is "a"
class b(a):
    a,b=100,200
    def m2(self):
        print(b.a-b.b)    #class variable called through class which is "b"
class c(b):
    i,j=30,40
    def m3(self):
        print(c.i*c.j)    #class variable called through class which is "c"

obj=c()
obj.m1()
obj.m2()
obj.m3()
# ---------------------------------------------------
                                # HEIRARCHY INHERITANCE
# class a:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class b(a):
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
# class c(a):
#     i,j=30,40
#     def m3(self):
#         print(self.i*self.j)

# obj=b()
# obj.m1()
# obj.m2()

# obj=c()
# obj.m1()
# obj.m3()
# ---------------------------------------------------
                    # MULTIPLE INHERITANCE
# class a:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class b():
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
# class c(a,b):
#     i,j=30,40
#     def m3(self):
#         print(self.i*self.j)

# obj=c()
# obj.m1()
# obj.m2()
# obj.m3()

# ---------------------------------------------------
                        #EXAMPLE
# class a:
#     def m1(self):   #method overriding
#         print('m1 method class A')
# class b(a):
#     def m1(self):   #method overriding 
#         print('m1 method class b')
#         super().m1()    #SUPER keyword use to invoke parent class method 
# obj=b()
# obj.m1()

# ---------------------------------------------------
                        #EXAMPLE
# class a:
#     a,b=10,20
# class b(a):
#     i,j=100,200
#     def m1(self,x,y):    
#         print(x+y)  #local variables
#         print(self.i+self.j)  #class variable & here we can access parent class variables in child class by using (self.)
#         print(self.a+self.b)  #class variable 
# obj=b()
# obj.m1(1000,2000)
# ---------------------------------------------------
                        #EXAMPLE
# class parent:
#     name='scott'
# class child(parent):
#     name='john'
# #now if we want to invoke parent class variable then we will make method and use super keyword
#     def m1(self):
#         print(super().name)

# obj=child()
# print(obj.name)
# obj.m1()

# ---------------------------------------------------
                        #EXAMPLE
# class a:
#     a,b,k=10,20,30   #class variable
#     def m1(self):
#         print(self.a+self.b+self.k)

# class b(a):
#     i,j,k=100,200,300     #class variable
#     def m1(self,x,y):   #local variable
#         print(x+y)      #local variable
#         print(self.i+self.j)
#         print(self.a+self.b+self.k) #here we can access parent class variables in child class by using (self.)
#         super().m1()    #SUPER keyword use to invoke parent class method 
#         print(super().k)      #overriding variables
#
# obj=b()
# obj.m1(1000,2000)
# ---------------------------------------------------
                        #EXAMPLE
# class bank:
#     def RateOfInterest(self):
#         return 0
# class xbank(bank):
#     def RateOfInterest(self):
#         return 20
# class ybank(bank):
#     def RateOfInterest(self):
#         return 30
    
# obj=ybank()
# print(obj.RateOfInterest())

# obj=xbank()
# print(obj.RateOfInterest())

# ---------------------------------------------------
                            #OVERLOADING (POLYMORPHISM) 
#POLYMORPHISM WE CAN IMPLEMENT USING OVERLOADING CONCEPT

# class human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print('hello' +name)
#         else:
#             print('helloooooo')
# obj=human()
# obj.sayhello('scott')   #overloading (1 method using in different ways)
# obj.sayhello()          #overloading (1 method using in different ways)

# ---------------------------------------------------
                            #OVERLOADING

# class calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
# obj=calculation()
# obj.add()
# obj.add(10,20)
# obj.add(10,20,30)






























































