# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def diameter(root):
            if not root:
                return 0
            left_depth = diameter(root.left)
            right_depth = diameter(root.right)
            self.ans = max(left_depth+right_depth+1, self.ans)
            return max(left_depth, right_depth) + 1
        diameter(root)
        return self.ans - 1


if __name__ == "__main__":
    s = Solution()
    root_node = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    root_node.left = a
    root_node.right = b
    a.left = c
    a.right = d
    print(s.diameterOfBinaryTree(root_node))
