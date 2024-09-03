import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search("\"http(s)?://(www.)?youtube.com/(.)*?\"",s)
    if match:
        group = match.group()
        group = group[1:]
        group = group[:len(group)-1:]
        group = group.replace("www.", "")
        group = group.replace("embed/", "")
        group = group.replace("http:", "https:")
        group = group.replace("youtube.com", "youtu.be")
        return group
    return None


if __name__ == "__main__":
    main()
