class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        # dp[i][j], the minimum hp required to survive at dungeon[i][j]
        # dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        rows = len(dungeon)
        columns = len(dungeon[0])
        dp = [[0] * (columns+1) for _ in range(rows+1)]
        dp[rows][columns-1] = 1
        dp[rows-1][columns] = 1
        for row in range(rows-1):
            dp[row][columns] = float('inf')
        for column in range(columns-1):
            dp[rows][column] = float('inf')
        for row in range(rows-1, -1, -1):
            for column in range(columns-1, -1, -1):
                dp[row][column] = max(min(dp[row+1][column], dp[row][column+1]) - dungeon[row][column], 1)
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))

