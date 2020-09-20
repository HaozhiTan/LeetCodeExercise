class Solution:
    def uniquePathsIII(self, grid) -> int:
        if not grid:
            return 0
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.ans = 0
        self.steps = 1
        for row in range(self.rows):
            for column in range(self.columns):
                if grid[row][column] == 1:
                    start_point = (row, column)
                elif grid[row][column] == 0:
                    self.steps += 1
                elif grid[row][column] == 2:
                    self.end_point = (row, column)

        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(curr_row, curr_column, curr_steps):
            if curr_row == self.end_point[0] and curr_column == self.end_point[1]:
                if curr_steps == self.steps:
                    self.ans += 1
                return
                # 4 directions
            for direction in self.directions:
                next_row = curr_row + direction[0]
                next_column = curr_column + direction[1]
                if 0 <= next_row < self.rows and 0 <= next_column < self.columns and \
                        (grid[next_row][next_column] == 0 or grid[next_row][next_column] == 2):
                    grid[next_row][next_column] = 1
                    dfs(next_row, next_column, curr_steps + 1)
                    grid[next_row][next_column] = 0

        dfs(start_point[0], start_point[1], 0)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
    print(s.uniquePathsIII([[0, 1], [2, 0]]))
