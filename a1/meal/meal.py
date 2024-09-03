def main():
    time = input("What time is it?")
    converted = convert(time)

    if converted <= 8 and converted >= 7:
        print("breakfast time")
    elif converted <= 13 and converted >= 12:
        print("lunch time")
    elif converted <= 19 and converted >= 18:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    return float(hour + minute / 60)



# This makes sure that we only execute the main function when
# we are running the program, not when this module is imported
if __name__ == "__main__":
    main()
