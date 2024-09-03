from datetime import date, timedelta
import inflect
import sys

def season(year, month, day):
    dob_class = date(year, month, day)
    current_time = date.today()

    if dob_class > current_time:
            raise ValueError("Invalid Date :(")
    time_difference = current_time - dob_class
    total_minutes = time_difference.total_seconds() / 60

    p = inflect.engine()
    minutes_words = p.number_to_words(round(total_minutes))

    return minutes_words.capitalize().replace(" and", "")



def main():
    try:
        dob = input("Date of Birth (YYYY-MM-DD): ").strip()
        year, month, day = map(int, dob.split("-"))
        minutes_words = season(year, month, day)
        print(minutes_words + " minutes")
    except ValueError:
        sys.exit("Invalid Date :(")


if __name__ == "__main__":
    main()
