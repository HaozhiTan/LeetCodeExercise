from math import sqrt
import collections


class Solution:
    def largestComponentSize(self, A) -> int:
        # DSU algorithm
        max_element = max(A)
        dsu = DSU(max_element + 1)

        for a in A:
            for i in range(2, int(sqrt(a)) + 1):
                if a % i == 0:
                    dsu.union(a, i)
                    dsu.union(a, a // i)

        counter = collections.defaultdict(int)
        ans = 0
        for a in A:
            subset = dsu.find(a)
            counter[subset] += 1
            if ans < counter[subset]:
                ans = counter[subset]
        return ans


class DSU:
    def __init__(self, size):
        self.size = [1] * size
        self.rank = [1] * size
        self.parent = [i for i in range(size)]

    def find(self, u):
        # find the subset of u
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        rank_u = self.rank[root_u]
        rank_v = self.rank[root_v]
        if root_u == root_v:
            return
        if rank_u == rank_v:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
            self.size[root_u] += self.size[root_v]
        elif rank_u > rank_v:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        else:
            self.parent[root_u] = root_v
            self.size[root_v] + + self.size[root_u]


if __name__ == '__main__':
    s = Solution()
    print(s.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))
