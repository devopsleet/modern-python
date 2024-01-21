number = input("Please enter a series of numbers, using a separators  you like")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)
