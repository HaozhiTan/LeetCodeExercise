import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = collections.defaultdict(int)
        for j in J:
            d[j] = 1
        ans = 0
        for s in S:
            if d[s] == 1:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numJewelsInStones('aA', 'aAAbbbb'))
    print(s.numJewelsInStones('z', 'ZZ'))
