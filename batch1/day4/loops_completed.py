## Loops continuation

# use the break and continue statements
for i in range(2,10):
    print(i)
    if(i==7):
        break
else:
    print("Loop Complete properly")

# use a for loop over a collection
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days:
    print (d)

#using the enumerate() function to get index
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i, d in enumerate(days):
    print (i, d)
