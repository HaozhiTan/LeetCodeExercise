# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return self.ans

        def dfs(root, direction):  # direction = 0 refers from left, 1 from right
            if not root.left and not root.right:
                if direction == 0:
                    self.ans += root.val
                return
            if root.left:
                dfs(root.left, 0)
            if root.right:
                dfs(root.right, 1)

        dfs(root, -1)
        return self.ans
