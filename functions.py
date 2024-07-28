def multiply(x, y):
    result = x * y
    return result


answer = multiply(1, 2)
print(answer)



# forty_two = multiply(6,7)
# print(forty_two)


for val in range(1,5):
    two_times = multiply(2, val)
    print(two_times)


def modify_list(a_list):
    a_list = a_list + [5]
    print(a_list)


original_list = [1, 2, 3]
#print(original_list)
modify_list(original_list)
print(original_list)


def is_palindrome(string: str) -> bool:
    #backwards = string[::-1]
    return string[::-1].casefold() == string.casefold()


# word = input("Please enter the word to check = ")
# if is_palindrome(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))


def palindrome_sentence(string):
    new_alphanumeric_sentence = []
    for char in string:
        if char.isalnum():
            new_alphanumeric_sentence.append(char)
    new_sentence = ''.join(new_alphanumeric_sentence)
    print(new_sentence)
    if is_palindrome(new_sentence):
        print("is palindrome")
    else:
        print("It's not a palindrome")


sentence = input("Please write a sentence ")
palindrome_sentence(sentence)


def fibonacci(n):
    """
    Return the `n` th Fibonacci number
    :param n:
    :return:
    """
    if 0 <= n <= 1:
        return n

    n_minus_1, n_minus_2 = 1, 0

    result = None
    for f in range(n - 1):
        #print(n)
        result = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = result

    return result


for i in range(36):
    print(i+1, fibonacci(i))
