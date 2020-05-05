import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # # most intuitive way (a little bit slower)
        # char_frequency = collections.Counter(s)
        # ans = -1
        # for i, c in enumerate(s):
        #     if char_frequency[c] == 1:
        #         ans = i
        #         break
        # return ans

        # use list and set (a little bit faster)
        lst = []
        used = set()
        for c in s:
            if c in used:
                if c in lst:
                    lst.remove(c)
            else:
                lst.append(c)
                used.add(c)
        if lst:
            return s.index(lst[0])
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar(''))
    print(s.firstUniqChar('leetcode'))
    print(s.firstUniqChar('loveleetcode'))
