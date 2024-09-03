import sys
import csv
import tabulate

if len(sys.argv) != 2:
    sys.exit("Error! Incorrect number of arguements")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Error! Incorrect file format")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        reader = list(reader)
        header = reader.pop(0)
        print(tabulate.tabulate(reader, header, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("Error! File doesn't exist")
