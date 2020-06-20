from itertools import  permutations
from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums_list = list(range(1, n+1))
        ans = ''
        while n > 0:
            d = (k-1) // factorial(n-1)
            k -= d * factorial(n-1)
            n -= 1
            ans += str(nums_list[d])
            nums_list.remove(nums_list[d])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(4, 9))
    print(s.getPermutation(100, 125842394))
