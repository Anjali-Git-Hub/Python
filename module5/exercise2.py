# function that returns whether the number is odd or even

def odd_even(num):
    if num%2==0:
        return "even"
    return "odd"

numb=int(input("enter the number : "))
print(odd_even(numb))