from math import sqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for k in range(1, int(sqrt(i)) + 1):
                if dp[i - k * k] is False:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.winnerSquareGame(7))
    print(s.winnerSquareGame(4))
    print(s.winnerSquareGame(10000))
