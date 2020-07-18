from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # BFS
        graph = defaultdict(list)
        incoming_node = [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            incoming_node[v] += 1
        nodes = [idx for idx in range(len(incoming_node)) if incoming_node[idx] == 0]
        edges = len(prerequisites)
        ans = []
        while nodes and edges:
            node = nodes.pop()
            ans.append(node)
            for v in graph[node]:
                incoming_node[v] -= 1
                edges -= 1
                if incoming_node[v] == 0:
                    nodes.append(v)
        if edges:
            return []
        else:
            return ans + nodes


if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

