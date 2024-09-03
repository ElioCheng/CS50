amountDue = 50
print("Amount Due: 50")

while amountDue > 0:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amountDue -= coin
    else:
        print("Reject")
    if amountDue > 0:
        print("Amount Due:", amountDue)

print("Change Owed:",  (0 - amountDue))

