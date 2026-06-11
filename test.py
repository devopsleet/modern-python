class Solution:
    def backSpaceCompare(self, s:str, t:str)-> bool:


        def get_string(s:str)->str:
            skip = 0
            ans = []
            i = len(s) - 1
            while i >= 0:
                if s[i] == "#":
                    skip += 1
                elif skip > 0:
                    skip = skip - 1
                else:
                    ans.append(s[i])
                i = i - 1
            return "".join(reversed(ans))




        str1 = get_string(s)
        str2 = get_string(t)

        return True if str1 == str2 else False

S = Solution()
output = S.backSpaceCompare("##", "#")
print(output)
