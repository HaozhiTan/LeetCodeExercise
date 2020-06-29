import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # dp = [1] * n
        # for i in range(1, m):
        #     prev = dp.copy()
        #     for j in range(1, n):
        #         dp[j] = prev[j] + dp[j-1]
        # return dp[-1]
        # math solution
        # Note, that we need to make overall n + m - 2 steps,
        # and exactly m - 1 of them need to be right moves and n - 1 down steps.
        # By definition this is number of combinations to choose n - 1 elements from n + m - 2.
        return math.comb(n+m+2, n-1) # only available in python 3.8+


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))
    print(s.uniquePaths(7, 4))
    print(s.uniquePaths(7, 5))
    print(s.uniquePaths(7, 6))
    print(s.uniquePaths(3, 3))
    print(s.uniquePaths(1, 1))
    print(s.uniquePaths(100, 100))
