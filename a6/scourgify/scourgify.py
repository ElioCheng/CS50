import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Error! Incorrect number of arguements")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Error! Incorrect file format")


try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        with open(sys.argv[2], "w") as after_file:
            writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            reader = list(reader)
            reader.pop(0)
            for row in reader:
                last_name, first_name = row[0].split(",")
                first_name = first_name.strip()
                writer.writerow({"first": first_name,
                                 "last": last_name,
                                 "house": row[1]})

except FileNotFoundError:
    sys.exit("Error! File doesn't exist")

