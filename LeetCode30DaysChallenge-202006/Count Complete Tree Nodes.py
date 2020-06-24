# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # calculate the depth of tree
        # use binary format (e.g. 4(101), ignore first 1, 01 refers to left and then right to access 5)
        # and binary search to find how many nodes in the last level
        tree_height = 0
        search_node = root
        while search_node:
            tree_height += 1
            search_node = search_node.left
        if tree_height <= 1:
            return tree_height

        def find_path(num, root):
            for d in bin(num)[3:]:
                if d == '0':
                    root = root.left
                elif d == '1':
                    root = root.right
            if not root:
                return False
            else:
                return True

        # binary search
        left = 1 << (tree_height - 1)
        right = (1 << tree_height)
        while left + 1 < right:
            mid = (left + right) // 2
            if find_path(mid, root):
                left = mid
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(s.countNodes(root))

