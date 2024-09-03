import sys
import pyfiglet
from pyfiglet import Figlet

if len(sys.argv) != 3 and len(sys.argv) != 0:
    sys.exit("Incorrect number of arguments :(")
if len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("invalid usage")

try:
    if len(sys.argv) == 3:
        f = Figlet(font=sys.argv[2])
except pyfiglet.FontNotFound:
    sys.exit("invalid usage")

myInput = input("Input: ")

print(f.renderText(myInput))


