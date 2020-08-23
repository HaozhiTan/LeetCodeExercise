class StreamChecker:

    def __init__(self, words):
        # Trie tree
        # Because description asks us to search from tail, the last k characters queried, where k >= 1,
        # we build a trie and search word in reversed order to satisfy the requirement.
        self.word_dict = {}
        for word in words:
            d = self.word_dict
            word = word[::-1]
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['.'] = {}  # end sign of the word
        self.word_to_find = ''

    def query(self, letter: str) -> bool:
        self.word_to_find += letter
        pointer = self.word_dict
        for char in reversed(self.word_to_find):
            if char not in pointer:
                return False
            else:
                pointer = pointer[char]
                if '.' in pointer:
                    return True
        return False


if __name__ == '__main__':
    s = StreamChecker(["cd", "abc", "kl"])
    print(s.query('a'))
    print(s.query('b'))
    print(s.query('c'))
    print(s.query('d'))
    print(s.query('e'))
    print(s.query('f'))
    print(s.query('g'))
    print(s.query('h'))
    print(s.query('i'))
    print(s.query('j'))
    print(s.query('k'))
    print(s.query('l'))


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
