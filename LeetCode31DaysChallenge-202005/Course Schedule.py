from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # Topological sort problem
        # BFS
        # graph = defaultdict(list)
        # incoming_nodes = [0] * numCourses
        # edges = len(prerequisites)
        # for u, v in prerequisites:
        #     graph[u].append(v)
        #     incoming_nodes[v] += 1
        # nodes = [i for i in range(numCourses) if incoming_nodes[i] == 0]
        # while nodes and edges:
        #     node = nodes.pop()
        #     for v in graph[node]:
        #         incoming_nodes[v] -= 1
        #         edges -= 1
        #         if incoming_nodes[v] == 0:
        #             nodes.append(v)
        # if edges:
        #     return False
        # else:
        #     return True

        # DFS
        def iscycle(node):
            if visit[node] == 1:
                return True
            if visit[node] == 0:
                visit[node] = 1
                for v in graph[node]:
                    if iscycle(v):
                        return True
            visit[node] = 2
            return False

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        visit = [0] * numCourses
        for i in range(numCourses):
            if iscycle(i):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.canFinish(2, [[0, 1]]))
    # print(s.canFinish(2, [[0, 1], [1, 0]]))
    # print(s.canFinish(3, [[0, 1], [1, 0]]))
    print(s.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))
    print(s.canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))
