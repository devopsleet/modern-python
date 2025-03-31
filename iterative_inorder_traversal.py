from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(10)
two = TreeNode(4)
three = TreeNode(16)
four = TreeNode(2)
five = TreeNode(7)

root.left = two
root.right = three
two.left = four
two.right = five


# DFS inorder implementation using stack
class Solution:
    def getMinimumDiff(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = []
        values = []
        current = root

        while current or stack:
            # push all the left nodes to the stack
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            values.append(current.val)

            current = current.right

        ans = float('inf')
        for i in range(len(values) - 1):
            diff = abs(values[i] - values[i + 1])
            ans = min(diff, ans)

        return ans


sol = Solution()
result = sol.getMinimumDiff(root)
print(result)
