class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern):
            return False
        pattern_dict = {}
        word_dict = {}
        for idx, word in enumerate(words):
            if (pattern[idx] not in pattern_dict) and (word not in word_dict):
                pattern_dict[pattern[idx]] = word
                word_dict[word] = 1
            elif (pattern[idx] not in pattern_dict) and (word in word_dict):
                return False
            elif pattern_dict[pattern[idx]] != word:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern(pattern="abba", str="dog cat cat fish"))
    print(s.wordPattern(pattern="abba", str="dog cat cat dog"))
    print(s.wordPattern(pattern="aaaa", str="dog cat cat dog"))
    print(s.wordPattern(pattern="abba", str="dog dog dog dog"))
