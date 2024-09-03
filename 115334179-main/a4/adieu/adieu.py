name = []

try:
    while True:
        myInput = input("Name: ")
        name[len(name):] = [myInput]
except EOFError:
    pass

print("Adieu, adieu, to ",sep="", end="")

if len(name) == 1:
    print(name[len(name)-1], sep="", end="")
    exit()
elif len(name) == 2:
    print(name[0], " and ", name[len(name)-1], sep="", end="")
    exit()

for i in range(len(name)-1):
    print(name[i], ", ",sep="", end="")


print("and ", name[len(name)-1], sep="", end="")
