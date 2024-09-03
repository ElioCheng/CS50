import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    vec = ip.split(".")
    if len(vec) != 4:
        return False
    for element in vec:
        try:
            element = int(element)
            if element >= 0 and element <= 255:
                continue
            else:
                return False
        except ValueError:
            return False

    return True


if __name__ == "__main__":
    main()
