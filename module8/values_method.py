user_info={
    "name":"anjali",
    "Age":19,
    "fav_movies":["stars","moons","satellites"],
    "fav_cartoons":["shinchan","doremon"]
}

# values method in python 
user_info_val=user_info.values()
# print(user_info_val)

# all the values will print in the form of list  but they are not actually list , we can check it's type 
# print(type(user_info_val))  # it is of type dict_values 

# we cannot add or remove the elements in case of dict values like lists 
# but we can do looping in dict values

# for i in user_info_val:
#     print(i)

