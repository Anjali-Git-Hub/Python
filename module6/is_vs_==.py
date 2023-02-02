# == equality operator 
# fruits1=["apple","mango"]
# fruits2=["banana","orange","apple"]
# print(fruits1==fruits2)
# false


fruits1=["apple","mango"]
fruits2=["apple","mango"]
print(fruits1==fruits2)
# true
# because the data inside the list is same . equality operator checks the data,value


# but
# is -> it checks whether list1 and list2 are stored in the same place in memory
print(fruits1 is fruits2)
# false , because both the lists , fruits1 and fruits2 are separate objects