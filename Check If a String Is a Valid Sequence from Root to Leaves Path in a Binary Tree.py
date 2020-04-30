# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        self.len_arr = len(arr)
        self.check = False

        def dfs(root, index):
            if self.check or not root:
                return
            if root.val == arr[index]:
                if index == self.len_arr - 1:
                    if not root.left and not root.right:
                        self.check = True
                    return
                else:
                    dfs(root.left, index+1)
                    dfs(root.right, index+1)
            else:
                return
        dfs(root, 0)
        return self.check
