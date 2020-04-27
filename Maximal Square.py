class Solution:
    def maximalSquare(self, matrix) -> int:
        # dp
        # dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
        max_len = 0
        rows = len(matrix)
        if rows == 0:
            return 0
        columns = len(matrix[0])
        dp = [0] * (columns + 1)
        for i in range(rows):
            temp = dp[:]
            for j in range(columns):
                if matrix[i][j] == '1':
                    dp[j+1] = min(min(dp[j], temp[j]), temp[j+1]) + 1
                    if dp[j+1] > max_len:
                        max_len = dp[j+1]
                else:
                    dp[j+1] = 0
        return max_len * max_len


if __name__ == "__main__":
    s = Solution()
    m1 = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    m2 = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
    print(s.maximalSquare(m1))
    print(s.maximalSquare(m2))