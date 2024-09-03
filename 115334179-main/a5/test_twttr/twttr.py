

def main():
    input_string = input("Input:\n")
    print("Output: ", end="")
    shortened = shorten(input_string)
    print(shortened)

def shorten(word):
    shortened = ""
    for char in word:
        match char:
            case "A" | "E" | "I" | "O" | "U" | "a" | "e" | "i" | "o" | "u":
                pass
            case _:
                shortened += char
    return shortened

if __name__ == "__main__":
    main()
