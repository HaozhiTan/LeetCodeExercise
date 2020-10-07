# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        list_length = 0
        # find the length
        curr_node = head
        while curr_node:
            list_length += 1
            curr_node = curr_node.next
        k = k % list_length
        if k == 0:
            return head
        index = list_length - k
        curr_node = head
        while index > 1:
            curr_node = curr_node.next
            index -= 1
        next_node = curr_node.next
        ans = next_node
        curr_node.next = None
        while next_node.next:
            next_node = next_node.next
        next_node.next = head
        return ans