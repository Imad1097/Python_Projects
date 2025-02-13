                        #RANGE() FUNCTION IN PYTHON
#-----------------------------------------------
# print(list(range(10)))  #0.....10
# print(list(range(5,10)))      #5.......9
# #-----------------------------------------------
# #print only odd numbers in 1-10
# print(list(range(1,10,2)))
# #-----------------------------------------------
# #print only even numbers in 1-10
# print(list(range(2,10,2)))
# #-----------------------------------------------
# print(list(range(10,1,-1)))
# #-----------------------------------------------
# print(list(range(-10,-5)))
# #-----------------------------------------------
# print(list(range(-10,-5,2)))
#-----------------------------------------------
                    #WHILE LOOP
# i=1
# while i<=10:
#     print(i)
#     i=i+1
# print("done")
#-----------------------------------------------
#print (1-10) in descending order (10-1)
# i=10
# while i>=1:
#     print(i)
#     i=i-1
# print("success")
#-----------------------------------------------
                #FOR LOOP
# for i in range(10):
#     print(i)
# #-----------------------------------------------
# for i in range(1,11):
#     print(i)
#-----------------------------------------------
# for i in range(2,10,2): #even number
#     print(i)  
# #-----------------------------------------------
# for i in range(1,10,2): #odd numbers
#     print(i)  
#-----------------------------------------------
            #print (1-10) in descending order
# for i in range(10,0,-1):
#     print(i)
#-----------------------------------------------
# for i in range(5,101,5):
#     print(i)
#-----------------------------------------------
        #Jumping statements (Break)
# for i in range(1,10):
#     if i==5:
#         break
#     print(i)
# print("program exited")
# #-----------------------------------------------
#         #Jumping statements (continue)
# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)
# print("program exited")
#-----------------------------------------------
        #Jumping statements (continue)
# for i in range(1,10):
#     if i==5 or i==3 or i==7:
#         continue
#     print(i)
# print("program exited")
#-----------------------------------------------
        #Jumping statements (continue)
# for i in range(1,20,2):
#     if i==3 or i==5 or i==7:
#         continue
#     print(i)
# print("program exited")
#-----------------------------------------------
                    #NumbersDemo
                   
                    #Max Function
# print(max(10,20,30,40,50))
# print(max(1.2361235, 2.0001, 30.235, 0.40,5.0))
                   
                     #Min Function
# print(min(10,20,30,40,50))
# print(min(1.2361235, 2.0001, 30.235, 0.40,5.0))
#-----------------------------------------------
                    #StringsDemo
            #creating empty strings variables
# name=""
# name=''
# name=()
# name=str()
# str1="welcome"
# str1=str1+"to python"
# print(str1)

# str="welcome"
# print(str+" programming")

# str="welcome"
# print((str+" programming ") *2)
#-----------------------------------------------
                                #SLICING []
                                #starting index[0] include 
                                #Ending Index[1] exclude
str="welcome"
print(str[1:3])
print(str[:6])
print(str[2:])
print(str[1:-1]) # here -1 will remove 1 value from last
print(str[1:-2]) # here -1 will remove 2 value from last
#-----------------------------------------------
                      #ASCII CODE NUMBER ord() and chr()
# print(ord('A'))
# print(chr(65))
#-----------------------------------------------
                      # max(),  min() & len()
# print(max("abc"))
# print(min("abc"))
# print(len("abc"))
#-----------------------------------------------
                      # in, not in operators
# s=("welcome")
# print("come" in s)      #true
# print("lome" in s)       #false

# print("come" not in s)      #false
# print("lome" not in s)       #true
# #-----------------------------------------------
#                       # Strings comparison (true/false)
# print("tim" == "tie") #.
# print("free" != "freedom") #
# print("arrow" > "arron") #
# print("right" >= "left") #
# print("teeth" < "tee") #
# print("yellow" <= "fellow") #
# print("abc" > "") #
#-----------------------------------------------
                      #Testing Strings (true/false)
# s="welcome to python"
# print(s.isalnum())
# print("welcome".isalpha())
# print("2021".isdigit())
# print("first number".isidentifier())
# print(s.islower())
# print(s.isupper())
# print(" ".isspace())
#-----------------------------------------------
                                #Searching for substrigs
# s="welcome to python"
# print(s.endswith("thon"))
# print(s.startswith("welcoma"))
# print(s.find("to"))    # finds the particular string's position 
# print(s.find("python"))  #same as above but if string is not present is the main string it will return (-1)
# print(s.count("o"))     #how many time this character is repeated in the main_string.
#-----------------------------------------------
                                #CONVERTING STRINGS
# s="STRING IN PYTHON"

# s1=s.capitalize()  # only 1st character is capitalize
# print(s1)

# s2=s.title()    #all 1st character in string will be capitalized
# print(s2)

# s3=s.lower()    #all character in lower case       
# print(s3)

# s4=s.upper()    #all character in upper case   
# print(s4)

# s5=s.swapcase()      #all lower case to upper case & all upper case to lower case
# print(s5)

# s6=s.replace("IN", "ON")    #   "IN" will replace with "ON"
# print(s6)
#-----------------------------------------------
                                #Reverse a String
# s="welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print("reversed string is:",rev_str)                  #emoclew
#-----------------------------------------------
                        #same example above using SLICING
# s="welcome"
# rev_str=s[::-1]  #[starting point:Ending point:remove digit]----> [0:7:-1]
# print(rev_str)         # emoclew
#------------------------------------------------
# fruits =['orange','banana','mango','pinapple']
# for x in fruits:
#     print(x.upper())


