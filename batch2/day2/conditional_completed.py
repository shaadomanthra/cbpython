# # Conditional Statments

# if, else, elif
a = 1010
b=10

if(a>b):
	message = "A is greater than B"
elif(a==b):
	message = "A is same as B"
else:
	message = "A is less than B"

# single line code
message = "A is less than B" if(a<b) else "A is greater than B"

print(message)
