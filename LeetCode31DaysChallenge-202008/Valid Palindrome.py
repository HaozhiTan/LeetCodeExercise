import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # fast way to use re library to remove non-alphanumeric characters
        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s).lower()
        if not s:
            return True
        if s == s[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome('A man, a plan, a canal: Panama'))
