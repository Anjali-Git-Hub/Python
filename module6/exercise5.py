def common_finder(l1,l2):
    comman=[]
    for i in l1:
        if i in l2:
            comman.append(i)
    return comman
print(common_finder([1,2,5,8],[1,2,7,6]))