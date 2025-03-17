# usage of semicolons


print("abc");
print("def");

# semicolon is necessary

print("abc"); print("def")
print("abc"); print("venky"); print("gagan")


# indentation
# follows strict indentation

print("abc")
#    print("def")  # unexpect indent

welcome_message = "Welcome to Python class"
print(welcome_message)

# welcome message not allowed
_abc = 9
print(_abc)

#9abc not allowed

# only underscore is allowed
_ = 100
print(_)

# avoid using reserved keywords

# import keywords
import keyword
print(len(keyword.kwlist)) # 35 keywords in Python

# dont use inbuilt functions
print("ABC")

# python

# print = 10 # python allows it because of dynamic typing but now you cannot use the print as a function
a = 10
print(a)

name = "venky"

student_name = "abi"
name_length = len(name)

# try to avoid using capital letters

NUM = 10
print(NUM)

# single line comment


# Data Types

# Python inbuilt data types

# text

# str

# A string is a series of characters
new_string = "This is a string aaaaaaaaaaaaaaaaaaaaaaaaaaaaraewerwsewsfererttr"
new_string_2 = 'This is a string aaaaaaaaaaaaaaaaaaaaaaaaaaaaraewerwsewsfererttr'

print(id(new_string))
print(id(new_string_2))

message = "I have watched 'Indian-2' Audio launched yesterday"
print(message)

string_1 = "abc"
string_2 = "abc "

print(string_1 == string_2)

print(string_1 == string_2.rstrip())
# print(new_string)
# print(type(new_string_2))

# numeric

# int, float

# sequence

# list, tuple, range

# mapping

# dict, hashing

# boolean

# True or False

# None
# None

# set
