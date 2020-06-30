class Trie:
    def __init__(self):
        self.trie = {}
        self.end = '*'

    def insert(self, word):
        dictionary = self.trie
        for symbol in word:
            if symbol in dictionary:
                dictionary = dictionary[symbol]
            else:
                dictionary[symbol] = {}
                dictionary = dictionary[symbol]
        dictionary[self.end] = True


class Solution:
    def findWords(self, board, words):
        # trie(prefix tree) and dfs

        # create trie tree
        trie_dict = Trie()
        for word in words:
            trie_dict.insert(word)

        def dfs(i, j, d, current_string, board_check):
            # i,j refers to current coordinates
            # d refers to current trie tree
            # current_string records all the symbols have been transversed
            # board_check to check if this coordinates has been walked before
            if self.words_to_find == 0:  # if all words have been found
                return
            if '*' in d and '/' not in d:  # if a word in dictionary has been found and this word has not been found before
                self.words_to_find -= 1
                self.ans.append(current_string)
                d['/'] = True

            if i < 0 or j < 0 or i >= self.rows or j >= self.columns:  # if outside the board
                return
            elif board_check[i][j] or board[i][j] not in d:
                # if this coordinates have been walked before or there is no satisfied word in trie tree
                return

            board_check[i][j] = 1
            dfs(i + 1, j, d[board[i][j]], current_string + board[i][j], board_check)
            dfs(i, j + 1, d[board[i][j]], current_string + board[i][j], board_check)
            dfs(i - 1, j, d[board[i][j]], current_string + board[i][j], board_check)
            dfs(i, j - 1, d[board[i][j]], current_string + board[i][j], board_check)
            board_check[i][j] = 0

        self.rows = len(board)
        self.columns = len(board[0])
        self.words_to_find = len(words)
        self.ans = []
        is_checked = [[0 for column in range(self.columns)] for row in range(self.rows)]
        for row in range(self.rows):
            for column in range(self.columns):
                if self.words_to_find == 0:
                    return self.ans
                elif board[row][column] in trie_dict.trie:
                    dfs(row, column, trie_dict.trie, '', is_checked)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                      ["oath", "pea", "eat", "rain", 'vreateoaa']))
    print(s.findWords([["a", "a"]],
                      ["aaa"]))
