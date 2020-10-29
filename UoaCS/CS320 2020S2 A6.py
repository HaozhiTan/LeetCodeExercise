import sys
from collections import defaultdict
from functools import lru_cache


class NetworkFlowProblem:
    def __init__(self):
        self.graph_dict = defaultdict(int)
        self.questions_dict = defaultdict(list)
        self.question_names = []
        line = sys.stdin.readline().strip()
        nums = line.split(' ')
        self.total_questions = int(nums[0])
        self.needed_questions = int(nums[1])
        self.difficulties = sys.stdin.readline().strip().split(' ')
        self.topics = sys.stdin.readline().strip().split(' ')
        for _ in range(self.total_questions):
            question = sys.stdin.readline().strip().split(' ')
            self.graph_dict[(question[2], question[1])] = 1
            self.questions_dict[(question[2], question[1])].append(question[0])
            self.question_names.append(question[0])


    def question_matching(self):
        selected = [None] * self.needed_questions
        for u in range(self.needed_questions):
            seen = [False] * self.needed_questions
            questions_seen = [False] * len(self.question_names)
            if not self.dfs(u, selected, seen, questions_seen):
                return 'No'
        return 'Yes'

    # @lru_cache(None)
    def dfs(self, u, selected, seen, questions_seen):
        for v in range(self.needed_questions):
            if self.graph_dict[(self.difficulties[u], self.topics[v])] and not seen[v]:
                for question in self.questions_dict[(self.difficulties[u], self.topics[v])]:
                    if not questions_seen[self.question_names.index(question)]:
                        seen[v] = True
                        questions_seen[self.question_names.index(question)] = True
                        if selected[v] is None or self.dfs(selected[v], selected, seen, questions_seen):
                            selected[v] = u
                            return True
        return False


if __name__ == '__main__':
    test_cases = int(sys.stdin.readline().strip())
    for _ in range(test_cases):
        g = NetworkFlowProblem()
        print(g.question_matching())

