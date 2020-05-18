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
def main():
    hello_basic()
    hello_name("Teja")
    hello_in_french()

# invoke if the call is direct instead of module
if __name__=='__main__':main()
