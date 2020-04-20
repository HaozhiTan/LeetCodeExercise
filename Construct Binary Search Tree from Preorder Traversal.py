# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        i = 1
        while i < len(preorder):
            smaller_node = None
            while len(stack) > 0 and preorder[i] > stack[-1].val:
                smaller_node = stack.pop()
            if smaller_node == None:
                smaller_node = TreeNode(preorder[i])
                stack[-1].left = smaller_node
                stack.append(smaller_node)
            else:
                smaller_node.right = TreeNode(preorder[i])
                stack.append(smaller_node.right)
            i = i + 1
        return root

