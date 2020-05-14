## Loops continuation

# use the break and continue statements
# for i in range(0,10):
#     print(i)
#     if i==5:
#         break
# else:
#     print("The loop completed properly")

# use a for loop over a collection
list = ["one","two","three",'four']
for i in list:
    print(i)

#using the enumerate() function to get index
days =["mon","tue","wed","thur","fri","sat"]
for i,j in enumerate(days):
    print(i,j)
