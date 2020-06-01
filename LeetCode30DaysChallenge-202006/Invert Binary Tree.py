# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def swap(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            swap(root.left)
            swap(root.right)
        swap(root)
        return root


if __name__ == '__main__':
    s = Solution()
