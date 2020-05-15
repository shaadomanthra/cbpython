## Loops continuation

# use the break and continue statements
for i in range(10):
    print(i)
    if(i==5):
        break
else:
    print("The loop is executed properly")
# use a for loop over a collection
l1 = ['one','two','three','four','five']

for i in l1:
    print(i)

# using the enumerate() function to get index
for key,value in enumerate(l1):
    print(key,value)
