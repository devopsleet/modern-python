# Calculate the maximum depth of binary tree

from typing import Optional
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(0)
one = TreeNode(1)
Three = TreeNode(3)
Five = TreeNode(5)
Seven = TreeNode(7)

root.left = one
root.right = Three
Three.left = Five
Five.left = Seven


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = float('-inf')

        def dfs(node, depth):
            nonlocal maxDepth

            if not node:
                return
            if not node.left and not node.right:
                maxDepth = max(maxDepth, depth)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

            return

        dfs(root, 1)

        return maxDepth

s = Solution()
maxDepth = s.maxDepth(root)
print(maxDepth)

# Time Complexity = O(n)
# Space Complexity = O(n)
