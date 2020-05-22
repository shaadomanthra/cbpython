# Program to explain classes and objects

# basic class and object
class student:
    name=''
    rollnumber =''
    age = 0

    def __init__(self,n,a,r):
        self.name = n
        self.rollnumber = r
        self.age = a

    def getName(self):
        return self.name
## creation of objects
teja = student('Krishna Teja',29,1001)
print(teja.getName())

suresh = student('Suresh Kumar',30,1002)
print(suresh.getName())
