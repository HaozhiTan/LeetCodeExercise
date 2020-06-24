from math import factorial


class Solution:
    def numTrees(self, n: int) -> int:
        # dp
        # dp[n] = dp[0] * dp[n-1] + dp[1] * dp[n-2] + ... + dp[n-1] * dp[0]
        dp = [1] * (n+1)
        for node in range(2, n+1):
            s = 0
            for sub_node in range(0, node):
                s += dp[sub_node] * dp[node-1-sub_node]
            dp[node] = s
        return dp[n]
        # https://en.wikipedia.org/wiki/Catalan_number
        # return factorial(2*n) // (factorial(n+1) * factorial(n))


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3))
