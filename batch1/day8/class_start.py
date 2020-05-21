# Program to explain classes and objects

# basic class and object
# defenition of class
class student:
    name= ""
    age =""
    rollnumber = ""

    # constructor method
    def __init__(self,n,a,r):
        self.name = n
        self.age = a
        self.rollnumber = r

    def getRollNumber(self):
        return self.rollnumber
    def getAge(self):
        return self.age

teja = student("Teja",29,1001)

print(teja.getRollNumber())
print(teja.getAge())
