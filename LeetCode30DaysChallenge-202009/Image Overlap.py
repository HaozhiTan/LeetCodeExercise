from collections import defaultdict


class Solution:
    def largestOverlap(self, A, B) -> int:
        # linear transformation
        rows = columns = len(A)
        A_ones = []
        B_ones = []
        for row in range(rows):
            for column in range(columns):
                if A[row][column] == 1:
                    A_ones.append((row, column))
                if B[row][column] == 1:
                    B_ones.append((row, column))
        max_overlap = 0
        d = defaultdict(int)
        for x_a, y_a in A_ones:
            for x_b, y_b in B_ones:
                d[(x_a - x_b, y_a - y_b)] += 1
                max_overlap = max(max_overlap, d[(x_a - x_b, y_a - y_b)])
        return max_overlap


if __name__ == '__main__':
    s = Solution()
    print(s.largestOverlap(A=[[1, 1, 0], [0, 1, 0], [0, 1, 0]], B=[[0, 0, 0], [1, 0, 1], [1, 0, 0]]))
