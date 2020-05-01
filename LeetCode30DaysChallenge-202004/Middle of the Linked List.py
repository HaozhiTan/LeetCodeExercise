# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # count = 0
        # head_backup = head
        # while head:
        #     count += 1
        #     head = head.next
        # target = count // 2 + 1
        # head = head_backup
        # while target > 1:
        #     head = head.next
        #     target -= 1
        # return head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    a.next.next = c
    a.next.next.next = d
    print(s.middleNode(a).val)
