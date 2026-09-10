# fibonacci series with basic recursion

class Solution:
    def __init__(self):
        self.memo = {}

    def fibonacci(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.fibonacci(n-1) + self.fibonacci(n-2)

        return self.memo[n]


# T.C = O(n)
