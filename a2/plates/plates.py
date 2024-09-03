def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0].isalpha() or not s[1].isalpha():
        return False

    start_of_num = False
    first_num = True

    for char in s:
        if not char.isalnum():
            return False
        elif start_of_num and char.isalpha():
            return False
        elif char.isdigit() and first_num and char == "0":
            return False
        elif char.isdigit() and first_num and char != "0":
            start_of_num = True
            first_num = False
    return True



main()
