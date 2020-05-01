class Solution:
    def numIslands(self, grid) -> int:
        def dfs(i, j):
            if i < 0 or i >=self.row:
                return 
            if j < 0 or j >=self.col:
                return
            if grid[i][j] == '0':
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i-1, j)
            dfs(i+1, j)

        ans = 0
        self.row = len(grid)
        if self.row == 0:
            return ans
        self.col = len(grid[0])
        
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i,j)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1']]))
    print(s.numIslands([]))