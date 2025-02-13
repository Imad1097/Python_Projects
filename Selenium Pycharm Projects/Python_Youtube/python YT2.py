# a=100
# b=200
# print(a)
# print(b)
# del a
# #print(a) #IT WILL GIVE ERROR
# print(b)
#-----------------------------------------------
# a=5
# b=2
# print(a/b) #2.5
# print(a//b) #2 (quotient)
# print(a%b) #1 (remainder)
# print(a**b) #5 exponent 2 (25)
# #-----------------------------------------------
# name,age,sal='john',30,50000.50
# #print("name is:%s  age is:%d  salary is:%g" %(name,age,sal)) #APPROACH 01----> %s represents STRING, %d represents INTEGER, %g represents FLOAT
# print("name is:{}  age is:{}  salary is:{}" .format(name,age,sal)) #APPROACH 02---->
#-----------------------------------------------
# num1=input("enter first number")
# num2=input("enter first number")
# print(type(num1))
# print(type(num2))
# print(int(num1)+int(num2))
#-----------------------------------------------
# num1=int(input("enter first number"))
# num2=int(input("enter first number"))
# #print(type(num1))
# #print(type(num2))
# print(num1+num2)
#-----------------------------------------------
# num1=(input("enter first number"))
# num2=(input("enter first number"))
# print(int(num1) + int(num2))
#-----------------------------------------------
# num1=(input("enter first number"))
# num2=(input("enter first number"))
# print(float(num1) + float(num2))
#-----------------------------------------------
# a=[2,'a','abc',1.3,'TMC']
# if 'abc' in a:
#     print("available")
# else:
#     print("not available")
#----------------------------------------------
# age=15
# if age>=18:
#     print("eligible for vote")
# else:
#     print("not eligible for vote")
#-----------------------------------------------
# if True:
#     print("true condition")
# else:
#     print("false condition")
# #-----------------------------------------------
# if 1:
#     print("true condition")
# else:
#     print("false condition")
# #-----------------------------------------------
# if 0:
#     print("true condition")
# else:
#     print("false condition")
#-----------------------------------------------
#finds a number is even or odd #num%2==0
# num=13
# if(num%2==0):
#     print("Its even number")
# else:
#     print("Its odd number")
#-----------------------------------------------
#if else in single line (ternary operator)
# num=10
# print("even number") if num%2==0 else print("odd number")
#-----------------------------------------------
#multiple if else in single line
# num=11
# {print("even"), print("number")} if num%2==0 else {print("odd"), print("number")}
#-----------------------------------------------
# age=22
# if age>=23:
#     print("eligible for vote")  #will not check this block
# elif age<23:
#     print("not eligible for vote1")
# elif age<15:
#     print("not eligible for vote2")
# else:
#     print("not matching")    
#------------------------------------------------
#7
# multiple conditions using elif
# a=(int(input("enter number")))
# if a==1:
#     print("success")
# elif a==2:
#     print("fail_1")
# elif a==3:
#     print("fail_2")
# elif a==4:
#     print("fail_3")
# elif a==5:
#     print("fail_4")
# elif a==6:
#     print("fail_5")
# else:
#     print("invalid")