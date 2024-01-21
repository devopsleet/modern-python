# def is_palindrome(string):
#     # backwards = string[::-1]
#     # return backwards == string
#     return string[::-1].casefold() == string.casefold()
#
#
# word = input("Please enter a word to check ")
#
# if is_palindrome(word):
#     print("'{}' is a Palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


# sentence = "My name is Gagan"

#
def palindrome_sentence(string: str) -> bool:
    print(string)
    new_sentence = ""
    for ch in string:
        if ch.isalnum():
            new_sentence += ch
    return new_sentence[::-1].casefold() == new_sentence.casefold()


sentence = input('Please enter the sentence ')
if palindrome_sentence(sentence):
    print("is a sentence")
else:
    print("not a sentence")


def fibonacci(n: int) -> int:
    """
    Return the `n` th Fibonacci number, for positive `n`.
    :param n:
    :return:
    """

    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence(242)
