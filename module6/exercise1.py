# define a function that takes a list and return the square of the items of the list


def square(l): 
    squ=[]
    for i in l:
        squ.append(i*i)
    return squ
print(square([1,2,3,4]))

