import re

def main():
        print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([0-9]{1,2})(:([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(:([0-9]{2}))? (AM|PM)$"
    correct_format = re.search(pattern, s)

    if correct_format:
        from_hour_str = correct_format.group(1)
        from_minute_str = correct_format.group(3) or '0'
        from_period = correct_format.group(4)

        to_hour_str = correct_format.group(5)
        to_minute_str = correct_format.group(7) or '0'
        to_period = correct_format.group(8)

        if from_hour_str is None or to_hour_str is None:
            raise ValueError("Hour is missing.")

        from_hour = int(from_hour_str)
        if from_period == "PM" and from_hour != 12:
            from_hour += 12
        elif from_period == "AM" and from_hour == 12:
            from_hour = 0
        elif from_hour > 12 or from_hour < 0:
            raise ValueError
        to_hour = int(to_hour_str)
        if to_period == "PM" and to_hour != 12:
            to_hour += 12
        elif to_period == "AM" and to_hour == 12:
            to_hour = 0
        elif to_hour > 12 or to_hour < 0:
            raise ValueError

        from_minute = int(from_minute_str)
        to_minute = int(to_minute_str)

        if from_minute >= 60 or from_minute < 0 or to_minute >= 60 or to_minute < 0:
            raise ValueError

        return f"{from_hour:02}:{from_minute:02} to {to_hour:02}:{to_minute:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
