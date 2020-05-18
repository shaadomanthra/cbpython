## operating with files

reader = open("files/sample.txt","r")

# read and print lines
# for l in reader:
#     print(l)

# write data with single line
writer = open("files/new.txt",'w')
writer.write(reader.read())
# print(reader.read().rstrip())

# write files for multiline
# for line in reader:
#     writer.writelines(line)

# close files
reader.close()
writer.close()
