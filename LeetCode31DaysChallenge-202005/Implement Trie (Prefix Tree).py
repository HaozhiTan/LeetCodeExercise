class Trie:
    # Use Prefix Tree, dict of dict to track the words
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.end = '*'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_word = self.d
        for c in word:
            if c in current_word:
                current_word = current_word[c]
            else:
                current_word[c] = {}
                current_word = current_word[c]
        current_word[self.end] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_word = self.d
        for c in word:
            if c not in current_word:
                return False
            current_word = current_word[c]
        return self.end in current_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_word = self.d
        for c in prefix:
            if c not in current_word:
                return False
            current_word = current_word[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
