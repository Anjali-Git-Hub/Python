# question- take the input from the user 3 numbers and you hve to print average of three numbers using string formatting 
# bonus :- try to take all three comma separated input in one line

num_1,num_2,num_3=input("enter all 3 numbers ").split(",")

print(f"the average of {(int(num_1)+int(num_2)+int(num_3))/3}")