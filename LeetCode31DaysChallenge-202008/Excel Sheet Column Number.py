class Solution:
    def titleToNumber(self, s: str) -> int:
        reversed_s = s[::-1]
        ans = 0
        for power, c in enumerate(reversed_s):
            ans += (ord(c) - ord('A') + 1) * (26 ** power)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('A'))
    print(s.titleToNumber('AB'))
    print(s.titleToNumber('ZY'))
    print(s.titleToNumber('FXSHRXW'))