class Solution:
    def change(self, amount: int, coins) -> int:
        # dp[i][j] the number of ways to use first i coins get amount j
        # dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        dp = [1] + [0] * amount
        for i in range(1, len(coins)+1):
            for j in range(coins[i-1], amount+1):
                dp[j] += dp[j-coins[i-1]]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.change(amount=5, coins=[1, 2, 5]))
    print(s.change(amount=10, coins=[10]))
    print(s.change(amount=4, coins=[3]))
    print(s.change(amount=4, coins=[2]))
