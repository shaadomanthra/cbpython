## program to print different hello versions

# function to print message hello
def hello_basic():
    print("Hello")
# function to print hello and name
def hello_name(name):
    print("Hello "+name)
# function to print hello in french
def hello_in_french():
    print("Bonjour")

# invoke main function
def main1():
    print("Im invoked from hello.py")

def main2():
    print("Im invoked from module import")
# invoke if the call is direct instead of module
if __name__ == '__main__': main1()
