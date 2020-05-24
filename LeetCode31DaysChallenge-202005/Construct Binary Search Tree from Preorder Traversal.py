# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        def insert(root, node):
            if root.val > node.val:
                if not root.left:
                    root.left = node
                else:
                    insert(root.left, node)
            else:
                if not root.right:
                    root.right = node
                else:
                    insert(root.right, node)

        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            insert(root, TreeNode(preorder[i]))
        return root

