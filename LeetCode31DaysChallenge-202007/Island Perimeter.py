class Solution:
    def islandPerimeter(self, grid) -> int:
        # O(mn) loop solution
        rows = len(grid)
        columns = len(grid[0])
        perimeter = 0
        for row in range(rows):
            no_of_continuous_squares = 0  # count continuous squares in each row and add them up
            no_of_overlapped_squares = 0  # count overlapped squares in this row and previous row to remove overlapped sides
            for column in range(columns):
                if grid[row][column] == 0:
                    if no_of_continuous_squares > 0:
                        perimeter += no_of_continuous_squares * 2 + 2
                        no_of_continuous_squares = 0
                elif grid[row][column] == 1:
                    no_of_continuous_squares += 1
                    if row > 0 and grid[row - 1][column] == 1:
                        no_of_overlapped_squares += 1
            if no_of_continuous_squares > 0:
                perimeter += no_of_continuous_squares * 2 + 2
            perimeter -= 2 * no_of_overlapped_squares
        return perimeter


if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([[0, 1, 0, 0],
                             [1, 1, 1, 0],
                             [0, 1, 0, 0],
                             [1, 1, 0, 0]]))
    print(s.islandPerimeter([[1, 1, 0, 1],
                             [1, 1, 1, 1],
                             [0, 1, 0, 1],
                             [1, 1, 0, 1]]))
