from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # dfs
        self.word_dict = {}
        # @lru_cache(None)
        def dfs(i):
            if i in self.word_dict:
                return self.word_dict[i]
            if i == len(s):
                return True
            is_found = False
            for word in wordDict:
                if len(word) <= len(s) - i:
                    if word == s[i : i+len(word)]:
                        is_found = is_found or dfs(i + len(word))
            self.word_dict[i] = is_found
            return is_found

        return dfs(0)


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
    print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                      ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
