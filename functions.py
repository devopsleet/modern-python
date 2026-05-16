def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):

    return string[::-1].casefold() == string.casefold()
    # backwards = string[::-1]
    # return backwards == string
    #return string[::-1] == string
    # string.reverse(key=str.casefold)
    # return string[::-1] == string


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{} is not a palindrome".format(word))
