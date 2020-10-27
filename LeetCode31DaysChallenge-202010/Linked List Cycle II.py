class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p = head
        q = head
        while p != None and q is not None:
            p = p.next
            q = q.next
            if q is None:
                return None
            q = q.next
            if p == q:
                q = head
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None
