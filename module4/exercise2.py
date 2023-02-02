# ask the user to input a number containing more than one digit for example = 1567 
# calculate 1+5+6+7 and print their sum

# one hint:
# not convert the string into integer
# int(example[0]) + int(example[1])........+int(example(len(example)-1))


num=input("enter a number having more than one digit")
i=0
sum=0
while i<len(num):
    sum+=int(num[i])
    i+=1
print(f"the sum is {sum}");