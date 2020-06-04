class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        length = len(s)
        left = 0
        right = length - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(["h", "e", "l", "l", "o"]))
    print(s.reverseString(["H", "a", "n", "n", "a", "h"]))
