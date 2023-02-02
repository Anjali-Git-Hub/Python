user={
    'name':"anjali",
    "age":19,
    "fav_movies":["moon","stars","galaxy"]
}

copy_dict=user.copy()
print(copy_dict)

# now here copy_list and user are not the same dictionaries
# if we do something like this
 
copied=user
# now we can say that copied and user are same list
print(copied is user)
print(copy_dict is user)


# if a dictionary has two similar keys like
dict1={
    "name":"anjali",
    "age":19
}
dict2={
    "name":"yashika"
}
# print(dict1.update(dict2))
# print(dict1)
# dict1 name key will be overwrite by the name key of dict2

# print(dict1.append(dict2)) 
# so we can't use the append method in dictionaries


