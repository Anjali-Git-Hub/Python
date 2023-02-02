# 1. replace method
# message="hi i am Awsm what about you and i am cool also"
# print(message.replace(" ",""));
# print(message.replace(" ","_"))

# print(message.replace("am","you"))

#replace the first one "am"
# print(message.replace("am","you",1)); 


# replace the second one "am"
# print(message.replace("am","you",2));



# 2. find method
message="hi i am Awsm what about you and i am cool also"
# print(message.find("am"))

# i want the position of 2nd "am"
# print(message.find("am",6))  #34
# i give the position 6th that from position 6th you starts finding the "am" string 

# we can also find the position of a character
# print(message.find('c'));


# if i want to find the position of 2nd "am" in string without knowing the position of 1st "am" in the string so how to do that thing
pos_1=message.find("am");
# print(message.find("am",pos_1+1))

