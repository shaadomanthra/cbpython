# Program to explain classes and objects

# basic class and object
class student:
    name= "Krishna Teja"
    rollnumber = 29

    def printFullName(self):
        print(self.name)

    def printRollNumber(self):
        print(self.rollnumber)

teja = student()
teja.printFullName()
teja.name = "Sri Krishna"
teja.printFullName()
teja.printRollNumber()

# Create class with constructor
class student:
    name = ''
    rollnumber = ''
    def __init__(self,name,rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def printFullName(self):
        print(self.name)

    def printRollNumber(self):
        print(self.rollnumber)

teja = student("Krishna Teja",1001)
teja.printFullName()

kumar = student("Rajesh Kumar",1001)
kumar.printFullName()
