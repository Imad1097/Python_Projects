#A list is a collection which is ordered and changeable. 
#In python list are written with square brackets [], list is mutable
#----------------------------------------
                    #HOW TO CREATE A LIST
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","cherry"]
# mylist3=["apple",10,"banana",20]
# mylist=[]

# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)
#----------------------------------------
                    #Accessing items from the list
# mylist=["apple","banana","cherry"]
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2 ])
#----------------------------------------
                    #Range of indexes
# mylist=["apple","banana","cherry","orange","kivi","melon","mango"]
# print(mylist[2:5])
# print(mylist[-4:-1])
#----------------------------------------
                    #change item value
# mylist=["apple","banana","cherry"]
# print(mylist)
# mylist[2]="orannge"     #this will change the value based on indexes
# print(mylist)
#----------------------------------------
                    #READ THE LIST ITEMS USING LOOP
# mylist=["apple","banana","cherry"]
# for i in mylist:
#     print(i)
#----------------------------------------
                    #CHECK IF THE ITEM EXIST IN THE LIST OR NOT
# mylist=["apple","banana","cherry"]
# if "apple" in mylist:
#     print("yes")
# else:
#     print("NO")
#----------------------------------------
                #LIST LENGTH (COUNTING NUMBER OF ITEMS IN A LIST)
# mylist=["apple","banana","cherry"]
# print(len(mylist))
#----------------------------------------
                #ADD ITEMS APPEND() & insert()
# mylist=["apple","banana","cherry"]
# mylist.append("orange")  #adding new item at the end of the list
# mylist.insert(1,"mango") #adding new item based on indexes
# print(mylist)
#----------------------------------------


#----------------------------------------
#pop() is specifically designed for removing and returning elements from a list, and it is more suitable when you want to retain the value of the removed element. 
#On the other hand, del is a more general statement that can be used for a variety of deletion operations, including removing elements from a list, deleting entire lists,
#or deleting variables.
#----------------------------------------


#----------------------------------------
                #REMOVE ITEMS FROM THE LIST---> POP()
# mylist=["apple","banana","cherry","orange","kivi","melon","mango"]
# mylist.pop(5) #removing the value based on indexing.
# print(mylist)
#----------------------------------------
                #REMOVE ITEMS FROM x LIST----> DEL()
# mylist=["apple","banana","cherry","orange","kivi","melon","mango"]
# del mylist[2] #here del command also removes the item based on index value
# print(mylist)
#----------------------------------------
                            #CLEAR()
# mylist=["apple","banana","cherry","orange","kivi","melon","mango"]
# mylist.clear()
# print(mylist)
#----------------------------------------
                            #COPY LIST 
#list()
# mylist1=["apple","banana","cherry","orange","kivi","melon","mango"]
# mylist2=list(mylist1) #The list() function is used to create a new list by taking the elements of mylist1. This is a common way to create a copy of a list in Python.
# print(mylist1)
# print(mylist2)
#----------------------------------------
                            #COPY LIST 
#copy()
# mylist1=["apple","banana","cherry","orange","kivi","melon","mango"]
# mylist2=mylist1.copy()
# print(mylist1)
# print(mylist2)
#----------------------------------------
                            #combine/join lists
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)
#----------------------------------------
                            #list using loop statements
# list1=["a","b","c"]
# list2=[1,2,3]
# for i in list2:
#     list1.append(i) #Inside the loop, the append() method is used to add each element i from list2 to the end of list1. This means that each integer in list2 is added to list1.
# print(list1)
#----------------------------------------
                            #USING EXTEND()
# list1=["a","b","c"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)
#----------------------------------------
                                #TUPLE
#A list is a collection which is ordered and unchangeable. 
#In python tuples are written with round brackets (), tuple is immutable
#we cannot modify existing value
#we cannot append new value
#we cannot insert a new value
#we cannot remove a value

# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# print(mytuple)
#----------------------------------------
                            #ACCESS TUPLE ITEMS THROUGH INDEX
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# print(mytuple[1])   #here index starts from 0
# print(mytuple[-1])
#----------------------------------------
                            #ACCESS RANGES OF VALUE THROUGH INDEX
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# print(mytuple[2:6])
# print(mytuple[-4:-1])
#----------------------------------------
                            #CHANGING TUPLE ITEMS
#By default tuple does not allow you to change values bcoz it is immutable but there is work around
# tuple----> list(modify)--->tuple
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# mylist=list(mytuple)
# mylist[3]="pinapple"
# mytuple=tuple(mylist)
# print(mytuple)
#----------------------------------------
                        #READING THE TUPLE ITEMS USING LOOP
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# for i in mytuple:
#     print(i)
#----------------------------------------
                        #CHECKING IF ITEM EXIST(SEARCHING OF ITEM IN TUPLE
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# if "orange" in mytuple:
#     print("yes")
# else:
#     print("no")
#----------------------------------------
                        #TUPLE LENGTH - COUNTING ITEMS IN TUPLE
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# print(len(mytuple))
#----------------------------------------
                        #ADD ITEMS TO TUPLE - NOT POSSIBLE BCOZ TUPLE IS IMMUTABLE - CANNOT CHANGE VALUE/ITEMS
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# mytuple[2]="pinapple" #TypeError Tuple object does not support items assignment
# print(mytuple) #ERROR
#----------------------------------------
                        #ADD ITEMS TO TUPLE
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# mylist=list(mytuple)
# mylist[3] = "pinapple"
# mytuple=tuple(mylist)
# print(mytuple)
#----------------------------------------
                        #COPYING TUPLE
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# mytuple2=mytuple
# print(mytuple2)
#----------------------------------------
                        #COPYING TUPLE 2nd method
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# mytuple2=tuple(mytuple)
# print(mytuple2)
#----------------------------------------
                        #REMOVING ITEMS FROM TUPLE --> NOT POSSIBLE BCOZ TUPLE IS IMMUTABLE
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# mytuple.remove("apple")  #INVALID ITS NOT POSSIBLE
# print(mytuple)   #invalid
#----------------------------------------
                        #REMOVING ITEMS FROM TUPLE --> NOT POSSIBLE BCOZ TUPLE IS IMMUTABLE
# mytuple=("apple","banana","cherry","orange","kivi","melon","mango")
# del mytuple  #INVALID
# print(mytuple)  #INVALID  #name 'mytuple' is not defined
#----------------------------------------
                        #JOIN/COMBINE TUPLE
# tuple1=(10,20,30)
# tuple2=('a','b','c')
# tuple3=tuple1+tuple2
# print(tuple3)
#----------------------------------------
                        #JOIN/COMBINE TUPLE
# tuple1=(10,20,30)
# tuple2=('a','b','c')
# if tuple1==tuple2:
#     print("tuples are equal")
# else:
#     print("Not Equal")







































   


