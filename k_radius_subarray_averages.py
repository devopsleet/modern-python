class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if not k:
            return nums

        ans = [-1] * len(nums)

        ws = 2 * k + 1

        if ws > len(nums):
            return ans

        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(k, len(nums) - k):
            lb, rb = i-k, i+k
            subArrSum = prefix[rb+1] - prefix[lb]
            ans[i] = subArrSum//ws

        return ans
