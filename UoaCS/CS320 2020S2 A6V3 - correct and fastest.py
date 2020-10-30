import sys
from collections import deque


class NetworkFlowProblem:
    def __init__(self):
        line = sys.stdin.readline().strip()
        nums = line.split(' ')
        self.total_questions = int(nums[0])
        self.needed_questions = int(nums[1])
        difficulties = sorted(sys.stdin.readline().strip().split(' '))
        topics = sorted(sys.stdin.readline().strip().split(' '))

        self.graph_size = 2 + len(set(difficulties)) + len(set(topics))
        self.graph = [[0] * self.graph_size for i in range(self.graph_size)]
        self.flow_graph = [[0] * self.graph_size for i in range(self.graph_size)]
        self.difficulty_dict = {}
        self.topic_dict = {}
        index = 1
        difficulties_list = list(set(difficulties))
        for difficulty in difficulties_list:
            self.difficulty_dict[difficulty] = index
            index += 1
        topics_list = list(set(topics))
        for topic in topics_list:
            self.topic_dict[topic] = index
            index += 1
        for difficulty in difficulties:
            self.graph[0][self.difficulty_dict[difficulty]] += 1
        for topic in topics:
            self.graph[self.topic_dict[topic]][self.graph_size - 1] += 1

        for _ in range(self.total_questions):
            question = sys.stdin.readline().strip().split(' ')
            if question[2] in self.difficulty_dict and question[1] in self.topic_dict:
                self.graph[self.difficulty_dict[question[2]]][self.topic_dict[question[1]]] += 1

    def dinics_algorithm(self, source, sink):
        max_flow = 0
        while self.bfs(source, sink):
            max_flow += self.dfs(source, sys.maxsize)
        if max_flow == self.needed_questions:
            return 'Yes'
        else:
            return 'No'

    def bfs(self, source, sink):
        queue = deque([source])
        self.level = [0] * self.graph_size
        self.level[source] = 1
        while queue:
            u = queue.popleft()
            for v in range(self.graph_size):
                if not self.level[v] and self.flow_graph[u][v] < self.graph[u][v]:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        if self.level[sink] > 0:
            return True
        else:
            return False

    def dfs(self, u, flow):
        if u == self.graph_size - 1:
            return flow
        t = flow
        for v in range(self.graph_size):
            if self.level[v] == self.level[u] + 1 and self.flow_graph[u][v] < self.graph[u][v]:
                min_flow = self.dfs(v, min(self.graph[u][v] - self.flow_graph[u][v], t))
                self.flow_graph[u][v] += min_flow
                self.flow_graph[v][u] -= min_flow
                t -= min_flow
        return flow - t


if __name__ == '__main__':
    test_cases = int(sys.stdin.readline().strip())
    for _ in range(test_cases):
        g = NetworkFlowProblem()
        print(g.dinics_algorithm(0, g.graph_size - 1))
