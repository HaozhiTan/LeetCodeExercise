# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # start_odd = head
        # if head:
        #     even_head = head.next
        # while start_odd:
        #     nxt = start_odd.next
        #     if nxt:
        #         odd_nxt = nxt.next
        #         if odd_nxt:
        #             start_odd.next = odd_nxt
        #             start_odd = odd_nxt
        #             nxt.next = odd_nxt.next
        #         else:
        #             # odd nodes none
        #             break
        #     else:
        #         # even nodes none
        #         break
        # if start_odd:
        #     start_odd.next = even_head
        if not head:
            return
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(s.oddEvenList(head).val)

