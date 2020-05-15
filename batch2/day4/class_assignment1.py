# Write a program to print names of months using lists and functions
# in different formats
# format 1 - Januaray, Febuary...December
# format 2 - Jan, Feb... Dec
# format 3 - 1 Jan,2 Feb,....12 Dec
months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

def format1():
    str = ''
    for m in months:
        str = str + m + ' '
    print(str)

def format2():
    str = ''
    for m in months:
        m = m[0:3]
        str = str + m  + ' '
    print(str)

def format3():
    str = ''
    for num,month in enumerate(months):
        print(num+1,month)

format3()
