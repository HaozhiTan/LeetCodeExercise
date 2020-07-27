# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        # dfs
        def dfs(inorder_list):
            # print(inorder_list, postorder)
            if len(postorder):
                node_value = postorder[-1]
                if node_value not in inorder_list:
                    return None
                node = TreeNode(node_value)
                postorder.pop()
                idx = inorder_list.index(node_value)
                node.right = dfs(inorder_list[idx + 1:])
                node.left = dfs(inorder_list[:idx])
                return node

        return dfs(inorder)


if __name__ == '__main__':
    s = Solution()
    print(s.buildTree([9, 3, 15, 20, 7],
                      [9, 15, 7, 20, 3]))
