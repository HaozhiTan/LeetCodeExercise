class Solution:
    def maxProfit(self, prices) -> int:
        # dp
        # dp[i][j] maximum profit with j transactions for first i days
        # mp[i][j] = max(dp[0][j], dp[1][j], ... , dp[i-1][j], dp[i][j])
        # dp[i][j] = max(dp[i-1][j], mp[i-1][j-1]) + diff[i]
        # mp[i][j] = max(mp[i-1][j], dp[i][j])
        if len(prices) <= 1:
            return 0
        diff = []
        sign = prices[1] - prices[0] < 0
        curr_sum = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            curr_sign = tmp < 0
            if curr_sign == sign:
                curr_sum += tmp
            else:
                diff.append(curr_sum)
                curr_sum = tmp
                sign = curr_sign
        diff.append(curr_sum)

        n = len(diff)
        k = 2
        dp = [[0] * (k + 1) for _ in range(n)]
        mp = [[0] * (k + 1) for _ in range(n)]

        dp[0][1] = diff[0]
        mp[0][1] = diff[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j], mp[i - 1][j - 1]) + diff[i]
                mp[i][j] = max(mp[i - 1][j], dp[i][j])
        return max(mp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 5, 7, -7, -4, -3, 10, 2, 7, -4, -8, 13, 15]))
    print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
