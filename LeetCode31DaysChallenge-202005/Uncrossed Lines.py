class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        # turn the question into Longest Common Subsequence
        # dp, if A[x] == B[y]: dp[x][y] = dp[x-1][y-1] + 1
        # if A[x] != B[y]: dp[x][y] = max(dp[x-1][y], dp[x][y-1])
        len_a = len(A)
        len_b = len(B)
        dp = [len_b * [0], len_b * [0]]
        for i in range(len_a):
            for j in range(len_b):
                if A[i] == B[j]:
                    if j > 0:
                        dp[1][j] = dp[0][j - 1] + 1
                    else:
                        dp[1][j] = 1
                else:
                    if j > 0:
                        dp[1][j] = max(dp[0][j], dp[1][j - 1])
                    else:
                        dp[1][j] = dp[0][j]
            dp[0] = dp[1].copy()
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxUncrossedLines([1, 2, 2, 2, 1, 2], [1]))
    print(s.maxUncrossedLines([1, 4, 2], [1, 2, 4]))
    print(s.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
    print(s.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
