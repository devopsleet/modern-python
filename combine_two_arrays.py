import math
import List
def kth_prime():

    k = int(input())

    ub = 5000

    prime = [False] * (ub + 1)

    for i in range(2,ub):
        prime[i] = True

    sq = int(math.sqrt(ub))

    for i in range(2, sq+1):
        if prime[i]:
            for j in range(i*i, ub,i):
                prime[j] = False

    print(sum(prime))
    for val in l:
        if sum(value) == k:
            return index




ans = kth_prime()
print(ans)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        n = len(nums)

        ans = [0] * n

        l = 0
        r = n - 1

        while (l <=r):
            if abs(nums[l]) >= abs(nums[r]):
                ans.append(nums[l] * nums[l])
                l = l + 1
            else:
                ans.append(nums[r] * nums[r])
                r = r - 1

        return ans.reverse()
