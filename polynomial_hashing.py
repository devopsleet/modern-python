string = input('Enter the String = ')

N = int(1e5)
P = 31
PP = [1] * (N+1)
M = int(1e9) + 7

for i in range(1, N+1):
    PP[i] = (PP[i-1] * P) % M


def hashing(s):
    ans = 0
    n = len(s)
    for i in range(n):
        ans = (ans + (ord(s[i]) - ord('a') + 1) * PP[i]) % M
    return ans


result = hashing(string)
print(result)


def count_unique_substrings(s):

    ans = set()
    n = len(s)

    last_hash = 0
    for i in range(n):
        for j in range(i,n):
            last_hash = last_hash + ()

    return ans.size()
