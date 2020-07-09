import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # bfs
        if not root:
            return 0
        queue = collections.deque([(root, 1, 1)])
        ans = 1
        current_level = 1
        level_start_num = 1
        while queue:
            current_node, position, level = queue.popleft()
            if level > current_level:
                current_level = level
                level_start_num = position
            ans = max(ans, position - level_start_num + 1)
            if current_node.left:
                queue.append((current_node.left, position * 2, level + 1))
            if current_node.right:
                queue.append((current_node.right, position * 2 + 1, level + 1))
        return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    print(s.widthOfBinaryTree(root))


