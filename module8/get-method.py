user={
    'name':"anjali",
    "age":19,
    "fav_movies":["moon","stars","galaxy"]
}
# print(user.get('name'))

# print(user.get('agee'))

# we can overwrite None by not found 
# print(user.get('agee','not found!'))

if user.get('agee'):
    print("key is present")
else:
    print("key is not present")

# basically none means false so else condition will execute