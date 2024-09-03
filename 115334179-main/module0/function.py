# We can add default value to our function
def hello(to="World"):
    print("Hello,", to)


name = input("What's your name?")
hello(name)
