file_path = 'file.txt'
open_file = open(file_path, 'r')
text = open_file.readlines()
print(text)
print(len(text))
print(text[0])

print(open_file)

open_file.close()
