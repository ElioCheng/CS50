myInput = input("Expression:").strip()

x, operator, y = myInput.split(" ")
x = int(x)
y = int(y)

match operator:
    case "+":
        print(float(x + y))
    case "-":
        print(float(x - y))
    case "*":
        print(float(x * y))
    case "/":
        print(float(x / y))
