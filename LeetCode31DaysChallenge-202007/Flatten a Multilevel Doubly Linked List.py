# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        # dfs
        if not head:
            return head
        def dfs(head):
            if not head:
                return []
            return [head] + dfs(head.child) + dfs(head.next)

        order = dfs(head)
        for node_index in range(len(order) - 1):
            order[node_index].next = order[node_index + 1]
            order[node_index + 1].prev = order[node_index]
            order[node_index].child = None
        order[node_index + 1].next = None
        order[node_index + 1].child = None
        return order[0]




