# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = head
        while curr:
            curr_next = curr.next
            prev, next_node = dummy, dummy.next
            while next_node:
                if next_node.val > curr.val:
                    break
                prev = next_node
                next_node = next_node.next
            curr.next = next_node
            prev.next = curr
            curr = curr_next
        return dummy.next
