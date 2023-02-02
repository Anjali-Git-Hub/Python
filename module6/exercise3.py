def reverse_items(l):
    str=[]
    for i in l:
        str.append(i[::-1])
    return str
print(reverse_items(['abc','tuv','xyz']))
