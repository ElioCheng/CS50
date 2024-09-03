import random


def main():
    myLevel = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(myLevel)
        y = generate_integer(myLevel)
        i = 0
        while True:
            try:
                print(x, "+", y, "= ", end="")
                myAnswer = int(input())
                if myAnswer == (x+y):
                    score += 1
                    break
                elif i < 2:
                    i += 1
                    print("EEE")
                else:
                    print(x, "+", y, "=", (x+y))
                    break
            except ValueError:
                i += 1
                print("EEE")
    print(score)

def get_level():
    while True:
        try:
            myLevel = int(input("Level: "))
            if myLevel >= 1 and myLevel <= 3:
                break
        except ValueError:
            pass
    return myLevel

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
