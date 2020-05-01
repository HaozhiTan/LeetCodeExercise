from itertools import zip_longest


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def findNextChar(s: str):
            skip = 0
            for i in reversed(s):  # s[::-1] is slow
                if i == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                elif skip == 0:
                    yield i

        return all(x == y for x, y in zip_longest(findNextChar(S), findNextChar(T)))


if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare(S="ab##", T="c#d#"))
