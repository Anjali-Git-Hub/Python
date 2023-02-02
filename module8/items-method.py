# items method - important method


user_info={
    "name":"anjali",
    "Age":19,
    "fav_movies":["stars","moons","satellites"],
    "fav_cartoons":["shinchan","doremon"]
}
# user_info_items=user_info.items()
# print(user_info_items)
# items method will print all the items in the list 
# as a list inside which multiple tuples are present

# like this --> [('name', 'anjali'), ('Age', 19), ('fav_movies', ['stars', 'moons', 'satellites']), ('fav_cartoons', ['shinchan', 'doremon'])]

# but they actually not are list we can check it's type
# print(type(user_info_items)) #so it is of type dict items


# now why it is useful??
# for key,value in user_info.items():
#     print(f"key is {key} value is {value}")


    # if we give only one variable
# for i in user_info.items():
    # print(i)  
# it will simply print all the tuples which are inside the list 
