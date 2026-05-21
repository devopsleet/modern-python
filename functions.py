import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (Stdin).

    The function will continue looping, and prompting
    the user, until a vailid `int` is entered.

    :param prompt: The string that the user will see, when they promped to enter the value
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("What you entered is not a valid number")


highest = 1000
answer = random.randint(1,highest)
print(answer)

guess = 0
print("Guess the number between 1 and {} ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done you have guessed it")
        break
    else:
        if guess > answer:
            print("Please guess lower")
        else:
            print("Please guess higher")

def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string)


# sentence = input("Enter your sentence ")
# if palindrome_sentence(sentence):
#     print("{} is a palindrome sentence".format(sentence))


ans = multiply(18,3)
print(ans)
