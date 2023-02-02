# define a function that checks the greatest among 3 numbers
def greater(a,b):
    if a>b:
        return a
    return b
def greater_three(a,b,c):
    return greater(greater(a,b),c)

num1,num2,num3=input("enter the 3 numbers separated by comma ").split(",")
print(greater_three(int(num1),int(num2),int(num3)))