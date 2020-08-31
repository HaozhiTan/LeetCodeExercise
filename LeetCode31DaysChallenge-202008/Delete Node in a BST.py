# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # no left child
            if not root.left:
                temp_node = root.right
                root = None
                return temp_node
            # no right child
            elif not root.right:
                temp_node = root.left
                root = None
                return temp_node

            min_right_subtree_node = self.findMinNode(root.right)
            root.val = min_right_subtree_node.val
            root.right = self.deleteNode(root.right, min_right_subtree_node.val)
        return root

    def findMinNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current


