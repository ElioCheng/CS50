def main():
    myInput = input("Greeting:").lower().lstrip()
    money = value(myInput)
    print(money)

def value(greeting):
    if greeting.startswith("hello") or greeting.startswith("Hello"):
        return "$0"
    elif greeting.startswith("h") or greeting.startswith("H"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
