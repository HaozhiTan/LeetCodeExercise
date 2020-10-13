# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # mergesort
        if not head or not head.next:
            return head
        slow_point = head
        fast_point = head
        prev = None

        # find the mid of the linked list
        while fast_point and fast_point.next:
            prev = slow_point
            slow_point = slow_point.next
            fast_point = fast_point.next.next

        # delink the first half and second half of the linked list
        prev.next = None
        left_head = head
        right_head = slow_point

        l = self.sortList(left_head)
        r = self.sortList(right_head)

        # merge two linked list
        d = ListNode(-1)
        count = 0
        while l and r:
            if l.val <= r.val:
                d.next = ListNode(l.val)
                l = l.next
            else:
                d.next = ListNode(r.val)
                r = r.next
            d = d.next
            if count == 0:
                merged_head = d
            count += 1

        if l:
            d.next = l
        if r:
            d.next = r
        return merged_head




