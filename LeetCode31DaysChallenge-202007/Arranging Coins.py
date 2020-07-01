import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # k = int(math.sqrt(n * 2))
        # while n > k * (k + 1) // 2:
        #     k += 1
        # if n == k * (k + 1) // 2:
        #     return k
        # else:
        #     return k - 1
        # binary search or math (ans = int((2*n+0.25)**0.5-0.5)
        return int(math.sqrt(2 * n + 0.25) - 0.5)


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(0))
    print(s.arrangeCoins(1))
    print(s.arrangeCoins(5))
    print(s.arrangeCoins(8))
    print(s.arrangeCoins(10))
