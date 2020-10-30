import sys

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

    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.graph_size)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                    # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.graph_size)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

                # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        if max_flow == self.needed_questions:
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    test_cases = int(sys.stdin.readline().strip())
    for _ in range(test_cases):
        g = NetworkFlowProblem()
        print(g.FordFulkerson(0, g.graph_size - 1))
