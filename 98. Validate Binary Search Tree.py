# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # in-order traversal
        in_order_traversal_list = []

        def in_order_traversal(root):
            if root:
                in_order_traversal(root.left)
                in_order_traversal_list.append(root.val)
                in_order_traversal(root.right)

        in_order_traversal(root)

        return in_order_traversal_list == sorted(in_order_traversal_list) and len(in_order_traversal_list) == len(set(in_order_traversal_list))
        # # min, max limit dfs (slower)
        # def dfs(root, lower_limit, upper_limit):
        #     if not root:
        #         return True
        #     if root.val <= lower_limit or root.val >= upper_limit:
        #         return False
        #     return dfs(root.left, lower_limit, root.val) and dfs(root.right, root.val, upper_limit)
        # return dfs(root, -float('inf'), float('inf'))


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    print(s.isValidBST(root))

