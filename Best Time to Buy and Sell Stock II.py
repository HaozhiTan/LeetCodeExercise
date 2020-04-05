class Solution:
    def maxProfit(self, prices) -> int:
        # len_prices = len(prices)
        # if len_prices <= 1:
        #     return 0
        # i = 0
        # profit = 0
        # while i < len_prices:
        #     if i == len_prices - 1:
        #         break
        #     j = i
        #     while (prices[j] < prices[j + 1]):
        #         j = j + 1
        #         if j == len_prices - 1:
        #             break
        #     profit = profit + (prices[j] - prices[i])
        #     i = j + 1
        # return profit
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = profit + prices[i] - prices[i-1]
        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([0, 1, 0, 3, 12]))
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
