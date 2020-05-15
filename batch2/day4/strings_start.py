## String manipulation

# operations on strings
s = 'hello'
print(s)
s1 = "apple".capitalize()
print(s1)
s1 = "apple".upper()
print(s1)

# Multiline strings
line = """This is my first Multiline

then here is the second Multiline

and then the third Multiline"""
print(line)

# format string
s = "My name is {}, and my age is {}".format("Teja",29)
print(s)

# format string shortcut
name = "Teja"
age = 29
s = f"Name: {name},Age: {age}"
print(s)

print(name + str(age))
