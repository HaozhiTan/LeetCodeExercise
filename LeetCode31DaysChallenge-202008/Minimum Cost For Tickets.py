class Solution:
    def mincostTickets(self, days, costs) -> int:
        # dp[i] refers to the minimum spend until ith day
        dp = [0] * (days[-1] + 1)
        for day in range(1, days[-1] + 1):
            if day not in days:
                dp[day] = dp[day - 1]
            else:
                days_7_before = day - 7
                days_30_before = day - 30
                if days_30_before >= 0:
                    dp[day] = min(dp[day - 1] + costs[0], dp[days_7_before] + costs[1], dp[days_30_before] + costs[2])
                elif days_7_before >= 0:
                    dp[day] = min(dp[day - 1] + costs[0], dp[days_7_before] + costs[1], dp[0] + costs[2])
                else:
                    dp[day] = min(dp[day - 1] + costs[0], dp[0] + costs[1], dp[0] + costs[2])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    # print(s.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
    # print(s.mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))
    print(s.mincostTickets([1, 4, 6, 7, 8, 20],
                           [7, 2, 15]))
