# why we use dictionaries 
# because lists re not enough to store the real world data for eg
user_info=["anjali","19",["stars","moons","satellites"],["shinchan","doremon"]]
# print(user_info)
# so this list contain the information of a user like his/her name,age,fav_movies,fav_cartoons

# but this is not a good way we can use dictionaries for it

user_info={
    "name":"anjali",
    "Age":19,
    "fav_movies":["stars","moons","satellites"],
    "fav_cartoons":["shinchan","doremon"]
}
# as dictionary is a collection of unordered items , it means there is no indexing in dictionaries 

#  dictionaries contain key and their values (key-value)pairs
# print(user_info)
# print(user_info["fav_movies"])   #it will print the value


# second way to create dictionaries
# user_info = dict(name="anjali",age=19,cartoon=["shinchan","doremon"])
# print(user_info)
# print(type(user_info))


# we can store anything in the dictionaries
user_info={
    "name":"anjali",
    "Age":19,
    "fav_movies":["stars","moons","satellites"],
    "fav_cartoons":["shinchan","doremon"]
}

# we can store dictionaries inside dictionaries
# user_info={
#     user1:{
#         # user1 information
#     },
#     user2:{
#         # user2 information

#     }
# }


# we can add the data inside an empty dictionary
user_info={}
user_info["name"]="anjali"
user_info["age"]=19
print(user_info)