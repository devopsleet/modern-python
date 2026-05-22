from collections import defaultdict

def mostDistinctChar(s: str, k :int) -> int:

    hashmap = defaultdict(int)

    l = 0
    ans = 0
    n = len(s)
    for r,char in enumerate(s):
        hashmap[char] += 1

        while len(hashmap) > k  and l < n:
            curr_char = s[l]
            l += 1
            hashmap[curr_char] -= 1
            if hashmap[curr_char] == 0:
                del hashmap[curr_char]

        ans = max(ans, r-l+1)

    return ans



ans  = mostDistinctChar("eceba",2)
print(ans)
