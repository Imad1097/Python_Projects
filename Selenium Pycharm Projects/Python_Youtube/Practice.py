# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# for i in myset:
#     print(i)
#------------
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# print("cherry" in myset)
#------------
# dict={1:'a',2:'b',3:'c'}
# print(dict)
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# print(mydict['brand'])
# print(mydict.get('year'))
# print(mydict)
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# mydict['model'] = 'honda'
# print(mydict)
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# for i in mydict:
#     print(i)
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# for i in mydict:
#     print(mydict[i])
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# for i in mydict.values():
#     print(i)
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# for i in mydict.items():
#     print(i)
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# if('year' in mydict):
#     print("yes")
# else:
#     print('No')
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# print(len(mydict))
#------------
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# mydict['registration'] = 'karachi'
# print(mydict)
#------------
# class myclass:
#     def m1(self):
#         pass
#     def m2(self,name):
#         print(name)
# obj = myclass()
# obj.m1()    #instance method
# obj.m2("ssuet")     #instance method
#------------

# i,j,k=10,20,30  #global variables
# class myclass:
#     a,b=40,50   #Class Variable
#     def add(self, x, y):    # x & y are local variables
#         print(x+y)  # x & y are local variables
#         print(self.a+self.b)    # a & b are class variable
#         print(self.i+self.j+self.k)  # i , j & K are global variables
#
# obj=myclass()
# obj.add(100,200)
#-----------------------------
# num = int(input())
# def m1():
#     rev_num = int(str(num)[::-1])
#     if num == rev_num:
#         print("palindrome found")
#     else:
#         print("Palindrome not found")
# m1()
#-----------------------------
# def palindrome(number):
#     rev_num = int(str(number)[::-1])
#     return number == rev_num
#
# number_to_check = 454
# if palindrome(number_to_check):
#     print("palindrome found")
# else:
#     print("palindrome not found")
#
# obj = palindrome(152)
# print(obj)
#-----------------------------
# def palindrome(number):
#     rev_str = int(str(number)[::-1])
#     if number == rev_str:
#         print("palindrome found")
#     else:
#         print("palindrome Not Found")
#
# palindrome(454)
#-----------------------------
# def palindrome():
#     number = input()
#     rev_str = int(str(number)[::-1])
#     if number == rev_str:
#         print("palindrome found")
#     else:
#         print("palindrome Not Found")
#
# palindrome()
#-----------------------------
# class emp:
#     def __init__(self,e_id,e_name,e_salary,a,b):
#         self.e_id1 = e_id
#         self.e_name1 = e_name
#         self.e_salary1 = e_salary
#         self.a = a
#         self.b = b
#     def func(self):
#         print(self.e_id1, self.e_name1, self.e_salary1)
#         return self.a + self.b
#
# obj = emp(1,"john",10000000,2,3)
# add = obj.func()
# print(add)
#-----------------------------

# class a:
#     def m1(self):
#         print("m2 method of class b")
#
# class b(a):
#     def __init__(self, c):
#         print("m1 method of class a", c)
#
# #obj = b(10)
# a.__init__(20)
# #obj.m1()

#-----------------------------

#num = 153
#-----------------------------
# tn = 10
# first = 0
# second = 1
# print('fionacci series')
#
# for i in range(tn):
#         print(first, end=" ")
#         temp = first
#         #print(temp, end=" ")
#         first = second
#         second = temp + second

#-----------------------------
# tn = int(input("enter number: "))
# first = 0
# second = 1
# print('fionacci series')
#
# for i in range(tn):
#         print(first, end=" ")
#         temp = first
#         #print(temp, end=" ")
#         first = second
#         second = temp + second
#----------------------------
# def fionacci(tn):
#     first = 0
#     second = 1
#     print('fionacci series')
#
#     for i in range(tn):
#         print(first, end=" ")
#         temp = first
#         #print(temp, end=" ")
#         first = second
#         second = temp + second
#
# fionacci(10)

#----------------------------------------
# n = 10
# a = 0
# b = 1
#
# for _ in range(n):
#     print(a, end=" ")   #0 0 0 0 0 0 0 0 0 0
#     a = b       #a=1
#     print(a, end=" ")
#     #b = a + b
# ----------------------------------------
# #def find_max(numbers):
#     max_num = numbers[3, 1, 4, 6, 5]  # Initialize max to the first element
#     for num in numbers:    # Iterate through each element
#         if num > max_num:  # Check if the current element is greater than max
#             max_num = num  # Update max if the condition is true
#     return max_num         # Return the maximum number
# #obj=find_max([3, 1, 4, 6, 5])
# #print(obj)
#-----------------------------------------------------
numbers = [3, 1, 4, 6, 5]
max_num = numbers[0]  # Initialize max to the first element

for num in numbers:    # Iterate through each element
    if num > max_num:  # Check if the current element is greater than max
        max_num = num  # Update max if the condition is true

print(max_num)  # Print the maximum number

#-----------------------------------------------------

numbers = [3, 1, 4, 6, 5, 6, 4, 18, 3, 6, 3, 3, 6, 2, 6]

# Calculate the middle index
middle_index = len(numbers) // 2

# Get the middle value
middle_value = numbers[middle_index]

print(middle_value)


# ----------------------------------------12
# numbers = list(map(int, input().split()))
# print(numbers)
