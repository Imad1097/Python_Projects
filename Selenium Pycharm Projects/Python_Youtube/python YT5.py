                                    #SETS
#SET: A set is a collection which is unordered and unidexed, In python sets are written in curley brackets {}.
#SET IS MUTABLE
#----------------------------------------------
                                    #SETS
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# print(myset)
#----------------------------------------
                            #ACCESS ITEMS FROM SETS
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# for i in myset:
#     print(i)
#----------------------------------------
                            #VALUE EXIST IN SETS OR NOT
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# print('banana' in myset)
# print('banana2' in myset)
#----------------------------------------
                            #ADDING ITEM TO SETS
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# myset.add("orange", "GRAPE","FRUITS") #set.add() takes exactly one argument# sets are unordered that y its added in any sequence.
# print(myset)  #INVALID
#----------------------------------------
                            #ADDING ITEM TO SETS
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# myset.add("GRAPE","orange", "apple") #set.add() takes exactly one argument# sets are unordered that y its added in any sequence.
# print(myset)
#----------------------------------------
                            #ADDING ITEM TO SETS
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# myset.add("orange") # sets are unordered that y its added in any sequence. (same added entry will not effect)
# print(myset)
#----------------------------------------
                            #USING "SET.UPDATE([])" ADDING MULTIPLE ITEM TO SETS
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# myset.update(["pinapple","grapes"]) # sets are unordered that y its added in any sequence.
# print(myset)
#----------------------------------------
                            #REMOVE ITEM FROM SET --> remove()
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# myset.remove("orange") #BOTH remove() & discard() ARE SAME EXCEPT NOT GIVING ERROR IN discard()
# print(myset)
#----------------------------------------
                            #REMOVE ITEM FROM SET -->  discard()
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# myset.discard("orange") #BOTH remove() & discard() ARE SAME EXCEPT NOT GIVING ERROR IN discard()
# print(myset)
#----------------------------------------
                            #CLEAR ALL ITEMS FROM SET
# myset={"apple","banana","cherry","orange","kivi","melon","mango"}
# myset.clear()
# print(myset)
#----------------------------------------
                            #JOINING  TWO SETS ---> union()
# set1={"a", "b", "c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)
#----------------------------------------
                            #update() in JOINING  TWO SETS
# set1={"a", "b", "c"}
# set2={1,2,3}
# set1.update(set2)
# print(set1)
#----------------------------------------
                            # '|' Operator in JOINING  TWO SETS
# set1={"a", "b", "c"}
# set2={1,2,3}
# set3=set1|set2
# print(set3)
#----------------------------------------
                                    #DICTIONARY
#A dictionary is a collection which is unordered, changeable(mutable) and indexed
#In python dictionaries are written with curly brackets & they have keys and values

# mydict={101:"x",102:"y",103:"z"}
# print(mydict)
#-----------------------------------------
                                    #ACCESS ITEMS FROM DICTIONARY 
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# print(mydict["brand"])
# print(mydict["model"])
# print(mydict["year"])
#-----------------------------------------
                                    #ACCESS ITEMS FROM DICTIONARY USING .get()
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# print(mydict.get("brand")) #we can also use .get() to extract values
# print(mydict.get("model"))
# print(mydict.get("year"))
#-----------------------------------------
                                    #CHANGE VALUES IN DICTIONARY
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# mydict["year"] = 2020
# print(mydict)
#-----------------------------------------
                                    #READING ITEMS FROM DICTIONARY USING LOOP (1)
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# for i in mydict:
#     print(i)  #prints only key from dictionary
#-----------------------------------------
                                    #READING ITEMS FROM DICTIONARY USING LOOP (2)
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# for i in mydict:
#     print(mydict[i]) #Prints only values from dictionary
#-----------------------------------------
                                    #READING ITEMS FROM DICTIONARY USING LOOP (2)
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# for i in mydict.values():
#     print(i) #Prints only values from dictionary
#-----------------------------------------
                                    #READING ITEMS FROM DICTIONARY USING LOOP (3)
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# for x,y in mydict.items():
#     print(x,y) #Printing keys along with the values
#-----------------------------------------
                                    #check key exist in dictionary or not
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# if "year" in mydict:
#     print("exist")
# else:
#     print("not exist")
#-----------------------------------------
                                    #FIND NUMBER OF ITEMS IN DICTIONARY
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# print(len(mydict))
#-----------------------------------------
                                    #ADDING ITEMS IN DICTIONARY
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021"}
# mydict["color"] = "silver"
# print(mydict)
#-----------------------------------------
                                    #REMOVE ITEMS FROM DICTIONARY
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021", "color":"silver"}
# mydict.pop("brand")
# del mydict["year"]
# print(mydict)
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021", "color":"silver"}
# print(mydict)
# mydict.clear()
# print(mydict)
#-----------------------------------------
                                    #COPYING DICTIONARY WITHOUT .copy() function
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021", "color":"silver"}
# mydict1=mydict
# print(mydict1)
#-----------------------------------------
                                    #COPYING DICTIONARY WITH .copy() function
# mydict={"brand":"suzuki", "model":"cultus", 'year':"2021", "color":"silver"}
# mydict1=mydict.copy()
# print(mydict1)



































































