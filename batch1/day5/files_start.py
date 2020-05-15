## operating with files

# reader = open('files/sample.txt','r')
# #read and print lines
# for line in reader:
#     print(line.rstrip())


# write files for multiline
reader = open('files/sample.txt','r')
writer = open('files/new.txt','w')
for l in reader:
    writer.writelines(l)
# write data with single line
reader = open('files/one.txt','r')
writer = open('files/one_new.txt','w')
writer.write(reader.read())

# close files
reader.close()
writer.close()
