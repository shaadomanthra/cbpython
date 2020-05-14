# # Functions in Python

# function with varaible arguments

# global & local variables
a=1
def func():
    global a
    a=20
    print(a)

func()
print(a)
