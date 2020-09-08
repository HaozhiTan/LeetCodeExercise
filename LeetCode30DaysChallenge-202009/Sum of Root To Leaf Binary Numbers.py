# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0

        def dfs(root, num):
            if not root.left and not root.right:  # leaf node
                self.ans += int(num, 2)
                return
            if root.left:
                dfs(root.left, num + str(root.left.val))
            if root.right:
                dfs(root.right, num + str(root.right.val))

        dfs(root, str(root.val))
        return self.ans


if __name__ == '__main__':
    s = Solution()
    node = TreeNode(1)
    node.left = TreeNode(0)
    node.right = TreeNode(1)
    print(s.sumRootToLeaf(node))
