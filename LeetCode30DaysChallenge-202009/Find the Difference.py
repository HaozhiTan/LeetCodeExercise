from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # d_s = Counter(s)
        # d_t = Counter(t)
        # for key, value in d_t.items():
        #     if (key not in d_s) or (key in d_s and value != d_s[key]):
        #         return key
        # XOR
        ans = 0
        for c in s:
            ans ^= ord(c)
        for c in t:
            ans ^= ord(c)
        return chr(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.findTheDifference(s="abcd",
                              t="abcde"))
