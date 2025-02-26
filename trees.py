class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, node):

        if not node:
            return 0

        left = self.maxDepth(node.left)
        print(left)
        right = self.maxDepth(node.right)
        print(right)

        return max(left, right) + 1

    @staticmethod
    def display(node, pointer):
        print(f"****************{pointer}*****************")
        while node:
            if pointer == 'left':
                print(node.val)
                node = node.left

            if pointer == 'right':
                print(node.val)
                node = node.right


root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)

root.left = one
root.right = two
one.left = three
one.right = four
two.right = five
five.right = six

Solution.display(root, "left")
Solution.display(root, "right")

s = Solution()
print("********MAX Depth********************")
result = s.maxDepth(root)

print(f"Max depth is {result}")
