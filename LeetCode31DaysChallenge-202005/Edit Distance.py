class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] the min operation to be two same words in first i-length word1 and j-length word2
        # if word[i] == word[j] then dp[i][j] = dp[i-1][j-1]
        # else dp[i][j] = min(dp[i-1][j], remove
        #                     dp[i-1][j-1], replace
        #                     dp[i][j-1], insert
        #                     ) + 1
        len_1 = len(word1)
        len_2 = len(word2)
        dp = list(range(len_2 + 1))
        for i in range(1, len_1 + 1):
            prev = dp.copy()
            for j in range(len_2 + 1):
                if j == 0:
                    dp[j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[j] = prev[j-1]
                    else:
                        dp[j] = min(prev[j], prev[j-1], dp[j-1]) + 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance('intention', 'execution'))
    print(s.minDistance('horse', 'ros'))



