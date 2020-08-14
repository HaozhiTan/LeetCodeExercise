from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        ans = 0
        odd_sum = 0
        for key, value in d.items():
            if value % 2 == 0:
                ans += value
            else:
                ans += value - 1
                odd_sum += 1
        if odd_sum >= 1:
            ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("aaaaabbbbbcccccddddd"))
    print(s.longestPalindrome('a'))
    print(s.longestPalindrome('ab'))
