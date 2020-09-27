from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        # graph + dfs
        graph = defaultdict(list)
        graph_values = {}
        for idx, edges in enumerate(equations):
            graph[edges[0]].append(edges[1])
            graph_values[(edges[0], edges[1])] = values[idx]
            graph[edges[1]].append(edges[0])
            graph_values[(edges[1], edges[0])] = 1 / values[idx]

        def dfs(current_point, goal_point, current_value, visited_points):
            if current_point in visited_points or current_point not in graph:
                return False
            visited_points.add(current_point)
            if current_point == goal_point:
                ans.append(current_value)
                return True
            for v in graph[current_point]:
                if dfs(v, goal_point, current_value * graph_values[(current_point, v)], visited_points):
                    return True

        ans = []
        for query in queries:
            start_point = query[0]
            end_point = query[1]
            visited = set()
            if start_point not in graph or end_point not in graph or not dfs(start_point, end_point, 1, visited):
                ans.append(-1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                         queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
