dictionary = {}

try:
    while True:
        currentItem = input().upper()
        if currentItem in dictionary:
            dictionary[currentItem] += 1
        else:
            dictionary[currentItem] = 1

except EOFError:
    pass

sorted_keys = sorted(dictionary)

for key in sorted_keys:
    print(dictionary[key], key)

