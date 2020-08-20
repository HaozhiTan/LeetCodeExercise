# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle, reverse the second half list, merge two list
        if not head:
            return head
        # find the middle
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half list
        prev = None
        current = slow.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # merge the list (everytime we move one step forward)
        slow.next = None
        first_half_head = head
        second_half_head = prev
        while second_half_head:
            next_node = first_half_head.next
            first_half_head.next = second_half_head
            first_half_head = second_half_head
            second_half_head = next_node

        return head


if __name__ == '__main__':
    s = Solution()