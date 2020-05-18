## dictionary - mutable
#
# data = {"name":"Teja","age":29,"address":"Hyderabad","Male":True}
#
# print(data['name'])
# # # print keys
# for key in data:
#     print(key,data[key])
#
# for i in data.keys():
#     print(i)
# # # print only values
# for i in data.values():
#     print(i)
# # # print key value pair
# for i,j in data.items():
#     print(i,j)
#
# # # changing values
# data['name'] = "Krishna"
# print(data)
#
# # # search key
# print('rollnumber' in data)
# # # search value
# print(30 in data.values())


## Sets - for unordered unique elements
a = set("2345782934")
b = set("371")
print(a | b)
print(a & b)
print(a - b)
