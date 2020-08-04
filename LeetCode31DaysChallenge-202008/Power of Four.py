from math import log


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        else:
            return log(num, 4) == int(log(num, 4))


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(15))
    print(s.isPowerOfFour(0))
    print(s.isPowerOfFour(1))
    print(s.isPowerOfFour(16))
    print(s.isPowerOfFour(4**15))
    print(s.isPowerOfFour(4**15+1))
