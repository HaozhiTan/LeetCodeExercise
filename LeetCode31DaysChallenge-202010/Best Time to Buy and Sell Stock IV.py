from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if 2 * k >= n:
            return sum(i-j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        profits = [0] * n
        for transaction_time in range(k):
            maximal_profit = 0
            for idx in range(1, n):
                profit = prices[idx] - prices[idx - 1]
                maximal_profit = max(maximal_profit + profit, profits[idx])
                profits[idx] = max(maximal_profit, profits[idx - 1])
        return profits[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
