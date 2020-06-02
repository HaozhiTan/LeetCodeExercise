# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # replace the current node with the next node and delete the next node
        # node.val = node.next.val
        # node.next = node.next.next
        node.val, node.next = node.next.val, node.next.next

