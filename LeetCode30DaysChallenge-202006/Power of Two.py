import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # ans = math.log2(n)
        # return ans == int(ans)
        return n > 0 and (n & (n-1) == 0)
