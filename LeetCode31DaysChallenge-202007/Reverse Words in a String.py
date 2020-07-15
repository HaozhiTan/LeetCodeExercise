class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split()
        s_list.reverse()
        return ' '.join(s_list)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("a good   example"))
    print(s.reverseWords("  hello  world!  "))
    print(s.reverseWords("  the sky      is   blue!     "))
