class Solution:
    def maxProfit(self, prices) -> int:
        # dp to calculate the continuous largest sum
        prices_diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        ans = 0
        dp = [0] * (len(prices_diff) + 1)
        for i in range(len(prices_diff)):
            dp[i + 1] = max(dp[i] + prices_diff[i], prices_diff[i])
            ans = max(dp[i + 1], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([100, 50, 40, 50, 0, 19]))
