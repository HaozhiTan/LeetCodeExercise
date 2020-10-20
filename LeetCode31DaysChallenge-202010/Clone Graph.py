from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        adj_list = defaultdict(list)
        deep_copy = {}
        visited = set()

        stack = [node]
        while stack:
            curr_node = stack.pop()
            deep_copy[curr_node.val] = Node(curr_node.val)
            if curr_node.val not in visited:
                visited.add(curr_node.val)
                for child_node in curr_node.neighbors:
                    adj_list[curr_node.val].append(child_node.val)
                    stack.append(child_node)

        for v in adj_list:
            curr_node = deep_copy[v]
            for child_node in adj_list[v]:
                curr_node.neighbors.append(deep_copy[child_node])
        return deep_copy[node.val]

