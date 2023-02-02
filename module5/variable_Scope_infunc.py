# def scope():
#     f=4
# print(f) 
 #error we cannot do this because the scope of variable f is within the function (local variable) only outside the function it is undefined

# f=4 #global variable
# def scope():
#     f=5 #local variable 
# print(f) #4 
# both variables are different 

x=6
def scope():
    global x
    x=4
    return x
print(x)  #6
print(scope()) #4
print(x) #4


