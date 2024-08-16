class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result.extend(word1[i])
                print(result)
            if i < len(word2):
                result += word2[i]

        return "".join(result)


S1 = Solution()
print(S1.mergeAlternately("abc", "def"))
