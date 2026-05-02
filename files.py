file_path = 'bookofdreams.txt'
open_file = open(file_path, 'r')
text = open_file.read()
print(len(text))
