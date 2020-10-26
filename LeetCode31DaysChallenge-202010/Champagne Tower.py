class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # simulation
        glass = [[0] * (i + 1) for i in range(query_row + 1)]
        glass[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                flow = (glass[i][j] - 1.0) / 2.0
                if flow > 0:
                    glass[i + 1][j] += flow
                    glass[i + 1][j + 1] += flow
        return min(1, glass[query_row][query_glass])


if __name__ == '__main__':
    s = Solution()
    # print(s.champagneTower(poured=2, query_row=1, query_glass=1))
    print(s.champagneTower(100000009, 33, 17))
