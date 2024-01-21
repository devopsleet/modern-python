panagram = """The quick 
brown fox jumps\tover 
the lazy dog"""

words = panagram.split()
separators = "."

numbers = "9,223,372,036,854,775,807"
generated_list = "".join(char if char not in separators else " " for char in numbers)
print(generated_list)

values = generated_list.split(",")
print(values)
# for index, value in enumerate(values):
#

for index, item in enumerate(values):
    values[index] = int(values[index])

print(values)

# creating a new list
integer_values = []
for value in values:
    integer_values.append(int(value))
print(integer_values)
