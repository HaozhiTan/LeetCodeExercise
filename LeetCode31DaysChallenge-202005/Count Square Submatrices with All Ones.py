class Solution:
    def countSquares(self, matrix) -> int:
        # if matrix[i][j] == 0: dp[i][j] = 0
        # if matrix[i][j] == 1: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        m, n = (len(matrix), len(matrix[0]))
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    ans += dp[i][j]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countSquares([
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]))
    print(s.countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]))
