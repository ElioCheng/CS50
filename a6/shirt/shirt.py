import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) != 3:
    sys.exit("Error! Incorrect number of arguements")
elif sys.argv[1].endswith((".jpg", ".jpeg", ".png")) == False or sys.argv[2].endswith((".jpg", ".jpeg", ".png")) == False:
    sys.exit("Error! Incorrect file format")
elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
    sys.exit("Error! Input and output file doesn't have the same format")

try:
    shirt = Image.open("shirt.png")
    image_before = Image.open(sys.argv[1])
    image_processed = ImageOps.fit(image_before, shirt.size)
    shirt.convert("RGBA")
    image_processed.convert("RGBA")
    mask = shirt.split()[3]
    image_processed.paste(shirt, mask)
    image_processed.save(sys.argv[2], format=image_processed.format)
except FileNotFoundError:
    sys.exit("Error! File doesn't exist")

