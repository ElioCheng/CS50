import sys

if len(sys.argv) != 2:
    sys.exit("Error! Incorrect number of arguements")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Error! Incorrect file name")

counter = 0
try:
    with open(sys.argv[1]) as file:
        for lines in file:
            if lines.lstrip().startswith("#"):
                pass
            elif lines.strip() == "":
                pass
            else:
                counter += 1
except FileNotFoundError:
    sys.exit("Error! File doesn't exist")

print(counter)




