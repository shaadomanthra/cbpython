## Exception handling in python

# basic
# try:
#     i = int("apple")
#     print(i)
# except:
#     print("There is an error")
#
# # Named errors
# try:
#     i = 10/5
#     print(i)
# except ValueError:
#     print("This is a value error")
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# except:
#     print("unknown error")
# else:
#     print("All is good")

# Error Reporting
def func(a):
    if(a==1):
        raise TypeError("The value of a cannot be 1")
    else:
        print(f"This number is good {a}")

try:
    func(1)
except TypeError as msg:
    print(msg)
