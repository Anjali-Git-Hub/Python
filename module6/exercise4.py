def even_odd(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output
print(even_odd([1,2,3,4,5,6,7]))
