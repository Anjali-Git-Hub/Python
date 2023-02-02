# split() method converts the string into list
# it will break the string from the point where it will get the space in between the string
# for example --> "anjali li"
# it will split the string between anjali and li as there is a space in between it 
# and store it in the list 
# like this --> ["anjali","li"]

# user_name="Anjali li".split()
# print(user_name)

# first_name,last_name="Anjali li".split() #["anjali","li"]
# print(first_name)
# print(last_name)

# first_name,last_name="Anjali,li".split(",") #["Anjali","li"]
# print(first_name)
# print(last_name)




# join method
# it will join the list data(must be string) in a single string 
# user_info=["anjali","19"]
# print(",".join(user_info))
# join the data of the list with comma 'anjali,19'

# user_info=["anjali",19] #all the data elements must be string
# print(",".join(user_info)) #error

user_info=["anjali","19"]
print(" ".join(user_info)) 

