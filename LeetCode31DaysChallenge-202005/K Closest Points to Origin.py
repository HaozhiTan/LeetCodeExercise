import heapq


class Solution:
    def kClosest(self, points, K: int):
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:K]


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
