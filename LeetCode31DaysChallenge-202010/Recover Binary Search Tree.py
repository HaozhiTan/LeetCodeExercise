# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [(root, 'init')] if root else []

        prev, first_error, second_error = None, None, None

        while stack:

            cur, state = stack.pop()

            if state == 'center':

                # catch error node during in-order traversal
                if not first_error and prev and prev.val > cur.val:
                    first_error = prev

                if first_error and prev and prev.val > cur.val:
                    second_error = cur

                prev = cur

            else:

                # in-order traversal with stack
                if cur.right:
                    stack.append((cur.right, 'right'))
                stack.append((cur, 'center'))
                if cur.left:
                    stack.append((cur.left, 'left'))

        # recover binary search tree with correct value by swap
        first_error.val, second_error.val = second_error.val, first_error.val

