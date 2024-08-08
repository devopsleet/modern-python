def check_if_palindrome(s):
    left = 0
    right = len(s) - 1
    count = 0
    while left < right:
        count += 1
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1

    return count


print(check_if_palindrome("abba"))
