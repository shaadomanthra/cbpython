## Program to understand modules

# import module and invoke function
# import hello
# hello.hello_in_french()
#
# # import with a name
import hello as h
h.hello_basic()

# import specific functions
from hello import hello_basic
hello_basic()

# import all function
from hello import *
hello_in_french()

# name of the module
import hello
if(hello.__name__ == 'hello'):
    hello.main2()
