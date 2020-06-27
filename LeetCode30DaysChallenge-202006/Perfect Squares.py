import math


class Solution:
    def numSquares(self, n: int) -> int:
        # # dp O(nlogn) dp[i] = Math.min(dp[i], dp[i - j * j]) for all j where j * j <= i
        # dp = [0]
        # for num in range(1, n+1):
        #     min_sum = float('inf')
        #     for i in range(1, int(math.sqrt(num))+1):
        #         current_sum = dp[num - i * i] + 1
        #         if current_sum < min_sum:
        #             min_sum = current_sum
        #     dp.append(min_sum)
        # return dp[-1]
        # First of all, there is a statement that any number can be represented as sum of 4 squares:
        # https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem. So, answer always will be 4?
        # No, when we talk about 4 squares, it means that some of them can be equal to zero.
        # So, we have 4 options: either 1, 2, 3 or 4 squares and we need to choose one of these numbers.
        #
        # How to check if number is full square? Just compare square of integer part and this number. Complexity of this part is O(1).
        # How to check if number is sum of 2 squares: n = i*i + j*j? iterate ovell all i < sqrt(n) and check that n - i*i is full square. Complexity of this part is O(sqrt(n)).
        # How to check that number is sum of 4 squares? In the same link for wikipedia:
        # by proving that a positive integer can be expressed as the sum of three squares if and only if it is not of the form 4^k(8m+7) for integers k and m. So, what we need to do is to check this condition and return true if it fulfilled. Complexity is O(log n)
        # Do we need to check anything else? No, because we have only one options left: 3 squares.
        # check one
        if int(math.sqrt(n)) ** 2 == n:
            return 1
        # check two
        for i in range(1, int(math.sqrt(n))+1):
            rest = n - i * i
            if int(math.sqrt(rest)) ** 2 == rest:
                return 2
        while n % 4 == 0:
            n //= 4
        if n % 8 != 7:
            return 3
        return 4


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))
    print(s.numSquares(13))
