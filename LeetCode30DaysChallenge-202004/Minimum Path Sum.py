class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = grid.copy()
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j-1>=0:
                        ans[i][j] = ans[i][j-1] + grid[i][j]
                    else:
                        ans[i][j] = grid[i][j]
                elif j == 0:
                    if i-1>=0:
                        ans[i][j] = ans[i-1][j] + grid[i][j]
                    else:
                        ans[i][j] = grid[i][j]
                else:
                    ans[i][j] = min(ans[i-1][j]+grid[i][j], ans[i][j-1]+grid[i][j])
        return ans[m-1][n-1]

if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
