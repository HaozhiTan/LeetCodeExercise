class Solution:
    def wordBreak(self, s: str, wordDict):
        cache = {}

        # dfs with memory cache
        def dfs(idx):  # return all the possibilities for s[i:]
            if idx in cache:
                return cache[idx]
            else:
                sentences = []
                for word in wordDict:
                    if idx + len(word) == len(s) and s[idx:] == word:  # reaching end
                        sentences.append(word)
                    elif idx + len(word) < len(s) and s[idx:idx+len(word)] == word:
                        following_sentences = dfs(idx+len(word))
                        for sentence in following_sentences:
                            sentences.append(word + ' ' + sentence)
                cache[idx] = sentences
                return sentences
        return dfs(0)


if __name__ == '__main__':
    s = Solution()
    # print(s.wordBreak(s="catsanddog",
    #                   wordDict=["cat", "cats", "and", "sand", "dog"]))
    # print(s.wordBreak(s="catsandog",
    #                   wordDict=["cats", "dog", "sand", "and", "cat"]))
    # print(s.wordBreak(s="pineapplepenapple",
    #                   wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
    # print(s.wordBreak(s="aaaaa",
    #                   wordDict=["a", 'aa']))
    print(s.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
