# define a function that takes a number n
# return a dictionary containing a cube of numbers from 1 to n
# for eg {1:1,2:8,3:27....n}

def cube_finder(n):
    cubes={}
    for i in range(0,n+1):
        cubes[i]=i**3
    return cubes
print(cube_finder(3))