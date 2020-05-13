# # Functions in Python

# function with varaible arguments
# def multiply(*args):
#     result = 1
#     for i in args:
#         result = result * i
#     return result
#
#
# print(multiply(2,3,4))

# global & local variables
a = 1
def func():
    global a
    a = 20
    print(a)

func()
print(a)
