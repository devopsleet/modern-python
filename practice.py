# # usage of semicolons
#
#
# print("abc");
# print("def");
#
# # semicolon is necessary
#
# print("abc"); print("def")
# print("abc"); print("venky"); print("gagan")
#
#
# # indentation
# # follows strict indentation
#
# print("abc")
# #    print("def")  # unexpect indent
#
# welcome_message = "Welcome to Python class"
# print(welcome_message)
#
# # welcome message not allowed
# _abc = 9
# print(_abc)
#
# #9abc not allowed
#
# # only underscore is allowed
# _ = 100
# print(_)
#
# # avoid using reserved keywords
#
# # import keywords
# import keyword
# print(len(keyword.kwlist)) # 35 keywords in Python
#
# # dont use inbuilt functions
# print("ABC")
#
# # python
#
# # print = 10 # python allows it because of dynamic typing but now you cannot use the print as a function
# a = 10
# print(a)
#
# name = "venky"
#
# student_name = "abi"
# name_length = len(name)
#
# # try to avoid using capital letters
#
# NUM = 10
# print(NUM)
#
# # single line comment
#
#
# # Data Types
#
# # Python inbuilt data types
#
# # text
#
# # str
#
# # A string is a series of characters
# new_string = "This is a string aaaaaaaaaaaaaaaaaaaaaaaaaaaaraewerwsewsfererttr"
# new_string_2 = 'This is a string aaaaaaaaaaaaaaaaaaaaaaaaaaaaraewerwsewsfererttr'
#
# print(id(new_string))
# print(id(new_string_2))
#
# message = "I have watched 'Indian-2' Audio launched yesterday"
# print(message)
#
# string_1 = "abc"
# string_2 = "abc "
#
# print(string_1 == string_2)
#
# print(string_1 == string_2.rstrip())
# # print(new_string)
# # print(type(new_string_2))
#
# # numeric
#
# # int, float
#
# # sequence
#
# # list, tuple, range
#
# # mapping
#
# # dict, hashing
#
# # boolean
#
# # True or False
#
# # None
# # None
#
# # set
#
#

# s1 = "flower"
# s2 = "fl"
#
# while not s2.startswith(s1):
#     s1 = s1[:-1]
#     print(s1)
#
# print(s1)
#
#
# s1 = "a"
# print(s1[0:0])

sentence = "i love eating burger"

words = sentence.split()

for index, word in enumerate(words):
    if word.startswith("burg"):
        print("yes")
        print(index + 1)
    else:
        print(word)


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Initialize the word position counter
        current_word_position = 1
        # Initialize the current index in the sentence
        current_index = 0
        # Get the length of the sentence
        sentence_length = len(sentence)

        # Loop through the sentence
        while current_index < sentence_length:
            # Skip leading spaces
            while (
                current_index < sentence_length
                and sentence[current_index] == " "
            ):
                current_index += 1
                current_word_position += 1

            # Check if the current word starts with searchWord
            matchCount = 0
            while (
                current_index < sentence_length
                and matchCount < len(searchWord)
                and sentence[current_index] == searchWord[matchCount]
            ):
                current_index += 1
                matchCount += 1

            # If the entire searchWord matches, return the current word position
            if matchCount == len(searchWord):
                return current_word_position

            # Move to the end of the current word
            while (
                current_index < sentence_length
                and sentence[current_index] != " "
            ):
                current_index += 1

        # If no match is found, return -1
        return -1
