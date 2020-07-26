class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))
    print(s.addDigits(1234))
