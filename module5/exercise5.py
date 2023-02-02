# pallindrome check

def pallindrome(a):
    return a==a[::-1]
naam=input("enter the string : ")
print(pallindrome(naam))
