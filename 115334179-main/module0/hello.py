# The prompt is just the arguement for input
# The actual value is the user input
name = input("What's your name?\n");

# This strip off the whitespaces on the left and right
# make sure what we have is the format that we want
name = name.strip();

# Capitalize the first letter of each word
name = name.title();

# format string
# If you put f at the beginning of the string, that indicates
# you want to be using variables in the string
print(f"Hello, {name}");


