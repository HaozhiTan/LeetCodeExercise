from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        values = []
        self.preorder(root, values)
        return ','.join(values)

    def preorder(self, root, values):
        if root:
            values.append(str(root.val))
            self.preorder(root.left, values)
            self.preorder(root.right, values)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data:
            values = data.split(',')
        else:
            values = []
        values_queue = deque(values)
        min_value = float('-inf')
        max_value = float('inf')
        return self.build_tree(values_queue, max_value, min_value)

    def build_tree(self, values, max_value, min_value):
        if values and max_value > int(values[0]) > min_value:
            value = int(values.popleft())
            root = TreeNode(value)
            root.left = self.build_tree(values, value, min_value)
            root.right = self.build_tree(values, max_value, value)
            return root
        else:
            return None


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
