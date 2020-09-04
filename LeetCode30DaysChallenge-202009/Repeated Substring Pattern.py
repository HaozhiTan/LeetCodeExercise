class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # method 1
        # n = len(s)
        # for i in range(1, n):
        #     if n % i == 0 and s[:i] * (n // i) == s:
        #         return True
        # return False
        # method 2
        return s in (s + s)[1:-1]


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern('abcab'))
