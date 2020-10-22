from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # if root.left and root.right:
        #     return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        # return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            for child in [node.left, node.right]:
                if not child:
                    continue
                queue.append((child, depth + 1))
