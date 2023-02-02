# add
user_info={
    "name":"anjali"
}

user_info["age"]=19
user_info["fav_food"]="maggie"
user_info["fav_cartoons"]=["shinchan","doremon"]
user_info["fav_places"]=("uttrakhand","mumbai","wholeworld")

# print(user_info)


# delete data--> pop()method
# user_info.pop("fav_places")
# print(user_info)

# pop method will remove the key-value pair and return the values of that key and we can also store these values

# poped_values=user_info.pop("fav_places")
# print(poped_values)


# if we donot pass any argument in pop method then a error will come
# user_info.pop()  #error , atleast one argument is mandatory to pass 
# print(user_info)


# but if we use popitem() method 

poped_items=user_info.popitem()
# now here no error will come , the pop method randomly remove any key-value pair and rturn the key- value pair and we can store the key-value pair as a poped items in a variable

print(poped_items)
