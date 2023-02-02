# if we want to check that this key is present in our list or not so for this we use in-keyword

user_info={
    "name":"anjali",
    "Age":19,
    "fav_movies":["stars","moons","satellites"],
    "fav_cartoons":["shinchan","doremon"]
}

# if 'name' in user_info:
#     print("present")
# else:print("not present")


# to check the values we use values()method

# if "anjali" in user_info.values():
#     print("present")

# if "neha" in user_info.values():
#     print("present")
# else:
#     print("absent")



# looping in dictionaries
for i in user_info:
    print(i)
    # all the keys will print 

# to print the values we can use values()method
for i in user_info.values():
    print(i)

