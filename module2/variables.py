# Why Python is called Dynamically Typed?
# Python variable assignment is different from some of the popular languages like c, c++ and java. There is no declaration of a variable, just an assignment statement.


name="anjali"
# print(name)  #anjali 
# here name is the variable that stores the value of string type 
# name=123
# we can change the value also 
# print(name)  #123


# we can declare more than one variable in a single line .
# name, age="anjali", 18
# print(name)
# print(age)

#  we can asign the same value to multple varibales in a single line
a=b=c=3
print(a+b+c);
# answer - 9

# more than one input in a single line
# name=input("enter your name");
# age=input("enter your age ");

# instead of taking input by using separate lines we can take the input in a single line  by using split function

# name,age=input("enter your name and age separate by space ").split()
# always uses space between name and age like -> anjali 18. NOT anjali18 , it will give error

# we can replace this space with comma
name,age=input("enter your name and age separated by comma").split(",")
# here only use comma b/w name and age. don't use space , it will give error here 