# def info(firstname,lastname,age=22):
#     print(firstname, lastname, age)
# info("anjali","li")
# info("anjali","li","35")

# def info(firstname,lastname,age=None):
#     print(firstname, lastname, age)
# info("anjali","li",45)
# info("anjali","li")

# def info(firstname,lastname="unknown",age=None):
#     print(firstname, lastname, age)
# info("anjali")




# def info(firstname,lastname="unknown",age): #error
#     print(firstname, lastname, age)
# info("anjali",23)

# so there is a rule in python if you want to make default param you have to make it at last , you can't make default parameter in between

# def info(firstname="anjali",lastname,age):  #error!!
#     print(firstname, lastname, age)