import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    all_occurences = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(all_occurences)


if __name__ == "__main__":
    main()
