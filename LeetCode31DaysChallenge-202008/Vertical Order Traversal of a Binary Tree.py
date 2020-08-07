from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode):
        # bfs
        q = deque([(root, 0, 0)])  # node, x, y
        nodes_info = []
        while q:
            current_node = q.popleft()
            nodes_info.append((current_node[0].val, current_node[1], current_node[2]))  # root.val, x, y
            if current_node[0].left:
                q.append((current_node[0].left, current_node[1] - 1, current_node[2] - 1))
            if current_node[0].right:
                q.append((current_node[0].right, current_node[1] + 1, current_node[2] - 1))
        nodes_info.sort(key=lambda tup: (tup[1], -tup[2], tup[0]))
        ans_dict = defaultdict(list)
        for node in nodes_info:
            ans_dict[node[1]].append(node[0])
        ans = []
        for key, values in ans_dict.items():
            ans.append(values)
        return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.verticalTraversal(root))