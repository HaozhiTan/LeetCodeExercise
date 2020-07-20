# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # prev = None
        # current = head
        # while current:
        #     if current.val == val:
        #         while current and current.val == val:
        #             current = current.next
        #         if not current:
        #             if prev:
        #                 prev.next = None
        #             else:
        #                 return None
        #         else:
        #             if prev:
        #                 prev.next = current
        #             else:
        #                 head = current
        #                 prev = current
        #                 current = current.next
        #     else:
        #         prev = current
        #         current = current.next
        # return head
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    s.removeElements(head, 1)

