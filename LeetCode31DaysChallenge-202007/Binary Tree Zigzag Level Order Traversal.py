from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        # bfs
        # odd level (left to right)
        # even level (right to left)
        q = deque([(root, 1)])
        previous_level = 1
        ans = []
        level_list = []
        if not root:
            return ans
        while q:
            current_node, current_level = q.popleft()
            if current_level == previous_level:
                level_list.append(current_node.val)
            else:
                if previous_level % 2 == 0:
                    level_list.reverse()
                ans.append(level_list)
                level_list = [current_node.val]
                previous_level += 1
            if current_node.left:
                q.append((current_node.left, current_level + 1))
            if current_node.right:
                q.append((current_node.right, current_level + 1))
        if current_level % 2 == 0:
            level_list.reverse()
        ans.append(level_list)
        return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.zigzagLevelOrder(root))
    print(s.zigzagLevelOrder(None))
