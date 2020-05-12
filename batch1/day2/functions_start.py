# # Functions in Python

# Basic function
def basic_function():
    print("This is a basic function")

basic_function()

# function with arguments
def arg(a,b):
    print(a,b)

arg(10,20)
# function with return value
def add(a,b):
    sum = a+b
    return sum
result = add(20,30)
print(result)

# function with default value
def power(n=2,p=1):
    result =1;
    for i in range(p):
        result  *=n # i=i+1 i+=1
    return result

print(power())
print(power())

# write a program with function to cube the number

# function with varaible arguments

# global & local variables
