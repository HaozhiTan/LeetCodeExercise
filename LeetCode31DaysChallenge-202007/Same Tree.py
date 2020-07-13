from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # # bfs
        # ans = True
        # queue_p = deque()
        # if p:
        #     queue_p.append(p)
        # queue_q = deque()
        # if q:
        #     queue_q.append(q)
        # while queue_p and queue_q:
        #     current_p = queue_p.popleft()
        #     current_q = queue_q.popleft()
        #     if current_p.val != current_q.val:
        #         ans = False
        #         break
        #     if current_p.left or current_q.left:
        #         if current_p.left and current_q.left:
        #             queue_p.append(current_p.left)
        #             queue_q.append(current_q.left)
        #         else:
        #             ans = False
        #             break
        #     if current_p.right or current_q.right:
        #         if current_p.right and current_q.right:
        #             queue_p.append(current_p.right)
        #             queue_q.append(current_q.right)
        #         else:
        #             ans = False
        #             break
        # if ans:
        #     if queue_q or queue_p:
        #         ans = False
        # return ans
        # dfs
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    s = Solution()
    print(s.isSameTree(None, None))
