class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Trie Tree
        self.word_dict = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        d = self.word_dict
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(w, current_word_dict):
            if not w:
                if '#' in current_word_dict:
                    return True
                else:
                    return False
            elif w[0] == '.':
                for key in current_word_dict.keys():
                    if dfs(w[1:], current_word_dict[key]):
                        return True
                return False
            elif w[0] not in current_word_dict:
                return False
            else:
                return dfs(w[1:], current_word_dict[w[0]])

        return dfs(word, self.word_dict)


if __name__ == '__main__':
    s = WordDictionary()
    s.addWord("bad")
    s.addWord("dad")
    s.addWord("mad")
    print(s.search("pad"))
    print(s.search("bad"))
    print(s.search(".ad"))
    print(s.search("b.."))
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)