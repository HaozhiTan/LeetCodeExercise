# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # # BFS
        # nodes = [root]
        # while nodes:
        #     xfound = yfound = False
        #     child_nodes = []
        #     for node in nodes:
        #         if node.val == x:
        #             xfound = True
        #         elif node.val == y:
        #             yfound = True
        #         if node and node.left and node.right:
        #             if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
        #                 return False
        #         if node.left:
        #             child_nodes.append(node.left)
        #         if node.right:
        #             child_nodes.append(node.right)
        #
        #     if xfound and yfound:
        #         return True
        #     elif xfound or yfound:
        #         return False
        #
        #     nodes = child_nodes.copy()
        # DFS (Can consider the binary tree as full binary tree) slower than BFS
        def dfs(root, pos):
            if not root:
                return
            if root.val == x:
                self.xpos = pos
            if root.val == y:
                self.ypos = pos
            dfs(root.left, pos*2)
            dfs(root.right, pos*2+1)
        dfs(root, 1)
        if self.xpos // 2 == self.ypos // 2:
            return False
        if len(bin(self.xpos)) != len(bin(self.ypos)):
            return False
        return True




