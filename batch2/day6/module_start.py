## Program to understand modules

# import hello
# # import module and invoke function
# hello.hello_basic()
# hello.hello_name("Teja")
# hello.hello_in_french()

# # import with a name
# import hello as h
# h.hello_basic()
#
# # import specific functions
# from hello import hello_basic
# hello_basic()
#
# # import all function
# from hello import *
# hello_in_french()

# name of the module
import hello
print(hello.__name__)

if(hello.__name__ == "hello"):
    print("This is from file")
