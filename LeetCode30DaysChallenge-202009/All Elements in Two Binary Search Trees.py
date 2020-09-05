# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        # BST can use inorder to return sorted list
        # use mergesort to combine two list
        def inorder(root, lst):
            if not root:
                return
            else:
                inorder(root.left, lst)
                lst.append(root.val)
                inorder(root.right, lst)
        list1 = []
        inorder(root1, list1)
        s1 = len(list1)
        list2 = []
        inorder(root2, list2)
        s2 = len(list2)
        p1 = p2 = 0
        ans = []
        while p1 < s1 and p2 < s2:
            if list1[p1] < list2[p2]:
                ans += [list1[p1]]
                p1 += 1
            else:
                ans += [list2[p2]]
                p2 += 1
        return ans + list1[p1:] + list2[p2:]


if __name__ == '__main__':
    s = Solution()
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)
    print(s.getAllElements(root1, root2))

