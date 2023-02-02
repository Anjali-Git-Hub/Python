def countr(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
print(countr([1,2,3,[3,4,5]]))