# Write a program to define a class name faculty with attributes
# name,department and age
# and functions inside class as getName,updateName
# then create an atleast two objects to test the functionality
class faculty:
    name=''
    department=''
    age=''

    def getName(self):
        return self.name

    def updateName(self,n):
        self.name = n

shyam = faculty()
shyam.name = "Shyam Kumar K"
print(shyam.getName())
shyam.updateName("Shyam K Kumar")
print(shyam.getName())
