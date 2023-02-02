# tuple with one element
name=("anjali")
# print(type(name))
# it is not a tuple at all , it is a string

name=(18)
print(type(name))
# it is a int not a tuple

name=("anjali",)
print(type(name))
# now it is a tuple . so whenever you will place one element inside the tuple , dont forget to place a comma after that

name=(18,)
print(type(name))
# tuple



# tuples without parenthesis
name="anjali",18,48.6
# print(type(name))


# unpacking of tuple
# user_name,age,marks=name
# print(user_name)
# print(age)
# print(marks)

# user_name,age=name  #error


# def sum_mul(i,j):
#     return (i+j),(i*j)

# this function returns two value in the form of tuple like this (value1,value2)
# print(sum_mul(2,3)) #(5,6)

# and we can also store these values separate in a varibale
# addition,multiply=sum_mul(2,3)
# print(addition)
# print(multiply)



# we can create tuples using range function 
# nums=tuple(range(1,11))
# print(nums)

# we can change a tuple into a list or str
mixed=("onion","raddish","apple",1,1.5,True,None,35+4j)
# print(list(mixed))
# but cannot change the actual tuple

# new_list=list(mixed)
# print(new_list)

# same we can use str () function to change the tuple into a string and can store it in a variable
new_string=str(mixed)
print(new_string)
print(type(new_string))
