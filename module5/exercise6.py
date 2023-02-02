# fibonnaci series

def fib(num):
    a=0
    b=1
    if num==1:
        print(a) 
    elif num==2:
        print(a, b) 
    else:
        print(a, b,end=" ")
        for i in range(num-2):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
    
number=int(input("enter the number upto which you want to print the fibonacci series "))
fib(5)