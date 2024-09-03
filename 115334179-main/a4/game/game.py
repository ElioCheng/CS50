import random

while True:
    try:
        my_level = int(input("Level: "))
        if my_level > 0 and my_level <= 100:
            break
    except ValueError:
        continue

number = random.randint(1, my_level)


while True:
    try:
        my_guess = int(input("Guess: "))
        if my_guess == number:
            print("Just right!")
            break
        elif my_guess < number:
            print("Too small!")
        else:
            print("Too large!")
    except ValueError:
        continue

