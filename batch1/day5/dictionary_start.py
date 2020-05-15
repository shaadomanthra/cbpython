## dictionary - mutable

# data = {"name":"Teja","age":29,"Address":"Hyderabad","Male":True}
# # print via index
# # print(data)
# # print(data['Address'])
#
# # print keys
# for i in data.keys():
#     print(i)
#
# # print only values
# for i in data.values():
#     print(i)
#
# # print key value pair
# for i,j in data.items():
#     print(i,j)
#
# # changing values
# data['name']="Krishna"
# print(data)
#
# # search key
# print('rollnumber' in data)
# # search value
# print('Hyderabad' in data.values())


## Sets - for unordered unique elements
a = set("2345192409")
b = set("367")
print(a & b)
print(a | b)
print(a - b)
