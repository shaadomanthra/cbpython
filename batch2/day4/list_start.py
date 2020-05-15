## Lists - mutable

# basic List


#print full list
# print(l)
#
# #print one element based on index
# print(l[9])
#
# # print few elements with start end
# print(l[2:8])
#
# # print elements with step
# l = [0,1,2,3,4,5,6,7,8,9]
# print(l[0:9:3])
l = [45,56,30,23,46,34,78,33,10,11]

# changing values
l[2]=100
print(l)
# adding elements at the end
l.append(200)
print(l)

# add element at a location
l.insert(3,50)
print(l)
# remove element
l.remove(46)
print(l)

# search for an element
i = l.index(78)
print(i)


# generate list with range function
r = list(range(50,61))
print(r)

## tuples - immutable
t = (1,2,3)

print(t[0])
t.append(10)
print(t)
