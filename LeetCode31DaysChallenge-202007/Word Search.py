class Solution:
    def exist(self, board, word: str) -> bool:
        self.rows = len(board)
        self.columns = len(board[0])
        word_length = len(word)

        def dfs(current_row, current_column, current_idx, goal):
            if self.is_found:
                return
            elif current_row < 0 or current_column < 0 or current_column >= self.columns or current_row >= self.rows:
                return
            elif board[current_row][current_column] == '#':
                return
            elif current_idx == goal and word[current_idx - 1] == board[current_row][current_column]:
                self.is_found = True
                return
            elif word[current_idx - 1] != board[current_row][current_column]:
                return
            tmp = board[current_row][current_column]
            board[current_row][current_column] = '#'
            dfs(current_row + 1, current_column, current_idx + 1, goal)
            dfs(current_row - 1, current_column, current_idx + 1, goal)
            dfs(current_row, current_column + 1, current_idx + 1, goal)
            dfs(current_row, current_column - 1, current_idx + 1, goal)
            board[current_row][current_column] = tmp

        self.is_found = False
        for row in range(self.rows):
            for column in range(self.columns):
                if board[row][column] == word[0]:
                    dfs(row, column, 1, word_length)
                    if self.is_found:
                        return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                  "ABCCED"))
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                  "SEE"))
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                  "ABCB"))