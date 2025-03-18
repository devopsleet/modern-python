# capitalize
# returns a new string
# first character is capital and all other characters in lowercase
# original string remains unchanged

s = "hello WORLD"
res = s.capitalize()
print(res)

# if first character is a number
s = "123hello WORLD"
res = s.capitalize()
print(res) # does not alter it because it only affects alphabetical characters

###############################
# casefold
# used to convert string to lowercase
# similar to lower() but is more aggressive in converting Unicode characters also

string1 = "straße"
string2 = "strasse"

print(string1.lower() == string2.lower())
print(string1.lower())
print(string1.casefold() == string2.casefold())


################################
# center
# center align strings
# center(length[, fillchar])
# fillchar is optional. If not provided, space is taken as default

a = "hello"
b = a.center(20, '-')
print(b)

##############################
# count
# returns the number of times a specified substring appears in a string
# count(substring, start = 0, end(len(s))

s = "hello world"
res = s.count("l")
print(res)
