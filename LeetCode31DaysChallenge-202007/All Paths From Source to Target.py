from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph):
        # dfs
        def dfs(current_node, path):
            if current_node == nodes - 1:
                self.ans.append(path)
                return
            for node in g[current_node]:
                dfs(node, path + [node])
            return

        nodes = len(graph)
        g = defaultdict(list)
        for u in range(len(graph)):
            for v in graph[u]:
                g[u].append(v)
        self.ans = []
        dfs(0, [0])
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))
