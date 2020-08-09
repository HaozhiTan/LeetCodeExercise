import copy


class Solution:
    def orangesRotting(self, grid) -> int:
        rows = len(grid)
        columns = len(grid[0])
        orange_left = 0
        for lst in grid:
            orange_left += lst.count(1)
        ans = 0
        while orange_left > 0:
            current_grid = copy.deepcopy(grid)
            previous = orange_left
            for row in range(rows):
                for column in range(columns):
                    if grid[row][column] == 2:
                        # check left side
                        if column - 1 >= 0 and grid[row][column - 1] == 1 and current_grid[row][column - 1] != 2:
                            orange_left -= 1
                            current_grid[row][column - 1] = 2
                        # check right side
                        if column + 1 < columns and grid[row][column + 1] == 1 and current_grid[row][column + 1] != 2:
                            orange_left -= 1
                            current_grid[row][column + 1] = 2
                        # check upper side
                        if row - 1 >= 0 and grid[row - 1][column] == 1 and current_grid[row - 1][column] != 2:
                            orange_left -= 1
                            current_grid[row - 1][column] = 2
                        # check down side
                        if row + 1 < rows and grid[row + 1][column] == 1 and current_grid[row + 1][column] != 2:
                            orange_left -= 1
                            current_grid[row + 1][column] = 2
            ans += 1
            grid = copy.deepcopy(current_grid)
            if previous == orange_left:
                return -1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(s.orangesRotting([[0, 2]]))
