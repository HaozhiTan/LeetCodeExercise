class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointer
        len_s = len(s)
        len_t = len(t)
        p_s = 0
        p_t = 0
        while p_s < len_s and p_t < len_t:
            if s[p_s] == t[p_t]:
                p_s += 1
            p_t += 1
        return p_s == len_s


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence(s="abc", t="ahbgdc"))
    print(s.isSubsequence(s="axc", t="ahbgdc"))
    print(s.isSubsequence(s="abc", t="ahcbgd"))
    print(s.isSubsequence(s="", t="ab"))
