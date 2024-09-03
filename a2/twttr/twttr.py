inputString = input("Input:\n")

print("Output: ", end="")
for char in inputString:
    match char:
        case "A" | "E" | "I" | "O" | "U" | "a" | "e" | "i" | "o" | "u":
             pass
        case _:
            print(char, end="")
