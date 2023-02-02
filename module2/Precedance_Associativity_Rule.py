# precedance order:-
# parenthesis > exponent > *, /, //, % > +,- 
# associativity left to right for all except exponent (right to left)

# question 1
# 5*5/2%6
# firstly *,/,% has same precedance so we see the associativity rule which is left to right

# 25/2%6
# 12.5%6

# print(5*5/2%6)
# print(12.5%6)



# question 2
# 2**3**2
# the associativity of exponent is right to left
# 3**2 -->9
# 2**9

print(2**3**2)
print(2**9)
