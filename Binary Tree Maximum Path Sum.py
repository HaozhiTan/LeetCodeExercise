# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -float('inf')

        def searchSum(root):
            if not root:
                return 0
            left_sum = max(searchSum(root.left), 0)
            right_sum = max(searchSum(root.right), 0)
            self.maxSum = max(left_sum + right_sum + root.val, self.maxSum)
            return max(left_sum, right_sum, 0) + root.val

        searchSum(root)
        return self.maxSum
