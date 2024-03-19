word_count= {}
text = "My name is Gagan"

for char in text.casefold():
    if char.isalnum():
        word_count[char] = word_count.setdefault(chr,0) + 1
