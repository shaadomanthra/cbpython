## Exception handling in python

# basic




#  Named errors
# try:
#     a = 10/2
#     print(a)
# except (ValueError):
#     print("We have encountered a value error")
# except ZeroDivisionError:
#     print("You cannot divide a number with zero.")
# except:
#     print("There is some error")
# else:
#     print("Successfully completed without errors")

# Error Reporting
def func(a):
    if(a==0):
        raise TypeError("The argument cannot be zero")
    print(a)
try:
    func(0)
except TypeError as msg:
    print(msg)
