from functools import reduce
from operator import xor
from collections import Counter


class Solution:
    def singleNumber(self, nums):
        # if need to use O(1) space, bit manipulation is required to solve this problem (68 ms)
        # s = reduce(xor, nums)
        # nz = s & (s-1) ^ s
        # num1 = reduce(xor, filter(lambda n: n & nz, nums))
        # return num1, s ^ num1
        # if use O(n) space, set could be the way (100 ms)
        d = Counter(nums)
        return list(dict(filter(lambda element: element[1] == 1, d.items())).keys())
        # d = sorted(d.items(), key=lambda dic: dic[1])
        # ans = [d[0][0], d[1][0]]
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 1, 3, 2, 5]))

