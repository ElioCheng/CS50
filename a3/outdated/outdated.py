month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        my_input = input("Date:").strip()


        if my_input[0].isalpha():
            month, date, year = my_input.split(" ")
            date = date[:-1]
            month = month_list.index(month) + 1
        else:
            month, date, year = my_input.split("/")

        date = int(date)
        year = int(year)
        month = int(month)

        if month <= 0 or month > 12 or date <= 0 or date > 31:
            raise ValueError

        print(year, "-", f"{month:02}", "-", f"{date:02}", sep="")
        break
    except ValueError:
        pass

