import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return math.pow(x, n)
        # return x ** n
        # recursive
        if n == 0:
            return 1
        elif n == 1:
            return x

        if n < 0:
            return self.myPow(1 / x, -1 * n)
        elif n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        else:
            return self.myPow(x, n // 2) ** 2 * x


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.00000, 10))
    print(s.myPow(2.10000, 3))
    print(s.myPow(2.00000, -2))
    print(s.myPow(2.00000, -2147483648))
    # print(s.myPow(99.99000, 2 ** 5))


