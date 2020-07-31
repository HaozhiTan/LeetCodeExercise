from math import sqrt


class Solution:
    def climbStairs(self, n: int) -> int:
        # # dp (fibo)
        # dp = [1] * (n + 1)
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]
        # math formula
        return round((0.5+sqrt(5)/2)**(n+1)/sqrt(5))


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(14))
