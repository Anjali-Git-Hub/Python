#question3- taje two comma seaprated input from user 
# 1. user's name 
# 2. a single character

# output-2 print lines 
# 1. user's name length
# 2. count the occurance of character in user's name that user inputed.

name,chr=input("enter your name and a single character separated by comma ").split(",")
# print(f"the length of the user's name is {len(name)}")
# print(f"the occurance of character is {name.upper().count(chr.upper())}")

#  Anjali, A if input like this . then the output will come 0 as our count method is taking " A" as a string  and finding it in our name string but there is not charcater like this 

# to solve this problem we remove the spaces

# by using strip method

# name.strip().upper().count(chr.strip().upper())
print(f"the length is {len(name.strip())}")
print(f"the occurance is {name.upper().count(chr.strip().upper())} ")