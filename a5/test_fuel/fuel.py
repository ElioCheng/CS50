import sys

def main():
    userInput = input("Fraction:")
    number = convert(userInput)
    result = gauge(number)
    print(result)


def convert(fraction):
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    how_much_left = int(round(x * 100 / y))
    return how_much_left



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99 and percentage <= 100:
        return "F"
    elif percentage > 100:
        raise ValueError
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
