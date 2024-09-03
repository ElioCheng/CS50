# integer casting here
x = int(input("What is x?\n"))
y = float(input("What is y?\n"))

# apply rounding to the fifth digit
z = round(x + y, 5)
print(z)

# print formatted result
# add comma
print(f"{z:,}")

# apply rounding using the f string
print(f"{z:.2f}")

