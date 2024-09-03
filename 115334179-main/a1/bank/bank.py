myInput = input("Greeting:").lower().lstrip()

if myInput.startswith("hello"):
    print("$0")
elif myInput.startswith("h"):
    print("$20")
else:
    print("$100")
