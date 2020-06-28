from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        # Euler Path
        # http://www.graph-magics.com/articles/euler.php
        # dfs
        def dfs(current_location):
            while self.graph[current_location]:
                next_location = self.graph[current_location].pop()
                dfs(next_location)
            self.ans.append(current_location)

        self.ans = []
        self.graph = defaultdict(list)
        for i, j in tickets:
            self.graph[i].append(j)
        for key in self.graph.keys():
            self.graph[key] = sorted(self.graph[key], reverse=True)
        dfs('JFK')
        return self.ans[::-1]


if __name__ == '__main__':
    s = Solution()
    # print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
