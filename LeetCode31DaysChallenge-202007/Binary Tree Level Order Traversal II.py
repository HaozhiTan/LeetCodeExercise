from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        # bfs
        if not root:
            return []
        d = deque([(root, 0)])  # node, level
        ans = []
        nodes = []
        current_level = 0
        while d:
            node, level = d.popleft()
            if level > current_level:
                ans.append(nodes)
                nodes = []
                current_level = level
            nodes.append(node.val)
            if node.left:
                d.append((node.left, level+1))
            if node.right:
                d.append((node.right, level+1))
        ans.append(nodes)
        ans.reverse()
        return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(5)
    print(s.levelOrderBottom(root))



