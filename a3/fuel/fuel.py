
while True:
    userInput = input("Fraction:")
    try:
        x,y = userInput.split("/")
        x = int(x)
        y = int(y)
        how_much_left = int(round(x * 100 / y))
        if how_much_left <= 1:
            print("E")
        elif how_much_left >= 99 and how_much_left <= 100:
            print("F")
        elif how_much_left > 100:
            raise ValueError
        else:
            print(how_much_left, "%", sep="", end="")
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
