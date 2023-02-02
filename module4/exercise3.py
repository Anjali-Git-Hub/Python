# ask a user for name 
# example anjali li
# print count of each word
# output
# a:2
# n:1
# j:1
# l:2
# i:2
#  :1
name=input("enter you full name ")
i=0
temp=""
while i<len(name):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1
