class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r, c):
            if r < 0 or c < 0 or r >= self.rows or c >= self.columns:
                return
            elif board[r][c] == 'X':
                return
            elif r == 0 or c == 0 or r == self.rows - 1 or c == self.columns - 1:
                self.is_valid = False
                return
            elif board[r][c] == 'T':
                return
            self.path.append((r, c))
            board[r][c] = 'T'
            dfs(r - 1, c)  # top
            dfs(r, c - 1)  # left
            dfs(r + 1, c)  # bottom
            dfs(r, c + 1)  # right

        self.rows = len(board)
        if self.rows:
            self.columns = len(board[0])
            for row in range(self.rows):
                for column in range(self.columns):
                    if board[row][column] == 'O':
                        if row == 0 or row == self.rows - 1 or column == 0 or column == self.columns - 1:
                            board[row][column] = 'T'
            for row in range(self.rows):
                for column in range(self.columns):
                    if board[row][column] == 'O':
                        self.path = []
                        self.is_valid = True
                        dfs(row, column)
                        if self.is_valid:
                            for r, c in self.path:
                                board[r][c] = 'X'
            for row in range(self.rows):
                for column in range(self.columns):
                    if board[row][column] == 'T':
                        board[row][column] = 'O'
        # return board


if __name__ == '__main__':
    s = Solution()
    print(s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
    print(s.solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]))
    

