input_string = input("camelCase:").strip()

for char in input_string:
    if char.isupper():
        print("_" + char.lower(), end="")
    else:
        print(char, end="")

