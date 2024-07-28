answer = 5

def get_integer(prompt):
    """
    Gets an integer from Standard Input(stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that the user will see,
        when they're prompted.
    :return: The integer that the user enters.

    """
get_integer()

print("Please guess the number between 1 and 10:")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("You have not guessed correctly")
else:
    print("You got it first time")
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
# else:
#     print("You got it first time")


def fibonacci
