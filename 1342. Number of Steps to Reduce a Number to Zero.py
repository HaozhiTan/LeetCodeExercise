import collections


class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        binary = bin(num)
        d = collections.Counter(binary[3:])
        ans = 1
        if '0' in d.keys():
            ans = ans + d['0']
        if '1' in d.keys():
            ans = ans + d['1'] * 2
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSteps(8))
    print(s.numberOfSteps(1))
    print(s.numberOfSteps(14))
