class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        diff = [prices[i + 1] - prices[i] for i in range(n - 1)]
        # dp[i] refers to maximum gain if use diff[i]
        # dp_max[i] refers to maximum gain no matter use diff[i] or not
        # put extra 2 element at the end to make sure i - 3 are in the range
        dp, dp_max = [0] * (n + 1), [0] * (n + 1)
        for i in range(n - 1):
            dp[i] = diff[i] + max(dp_max[i - 3], dp[i - 1])
            dp_max[i] = max(dp_max[i - 1], dp[i])
        return dp_max[-3]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))
    print(s.maxProfit([1, 2]))
