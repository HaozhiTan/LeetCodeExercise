# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # dfs
        # self.sum = 0
        # if not root:
        #     return 0
        # def dfs(root, string):
        #     if not root.left and not root.right:
        #         self.sum += int(string)
        #         return
        #     if root.left:
        #         dfs(root.left, string + str(root.left.val))
        #     if root.right:
        #         dfs(root.right, string + str(root.right.val))
        # dfs(root, str(root.val))
        # return self.sum
        if not root:
            return 0
        if not root.left and not root.right:
            return int(root.val)
        if root.left:
            root.left.val = 10 * root.val + root.left.val
        if root.right:
            root.right.val = 10 * root.val + root.right.val
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.sumNumbers(root))
