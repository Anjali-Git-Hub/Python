# In python we have some escape sequences 
# \'     ---> ''
# \"     ----> ""
# \n     -----> newline
# \b     -------> backspace
# \t     ---------> Tab
# \\     ------------> \

# print('i\'m anjali');
# will not give any error coz \' is an escape sequence that means ' .p

# similarly
# print("hello \"there\"")

# print("line A \nline B") 
# new line 

# print("anja\tli")

# print("hell\blo")

# print("this is a \ backslash")
# no error

# print("this is a backslash\");
#error why?? because here \"--> " . now the interpreter will get confused whether the line has complete or not so to avoid the error we uses \\ at there 

print("this is a backslash \\")
