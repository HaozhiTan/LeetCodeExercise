class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 1 ^ 1 = 0
        # 0 ^ 0 = 1
        # 0 ^ 1 = 1
        # 1 ^ 0 = 1
        return bin(x ^ y).count('1')

        # tricky way to find the difference in bits
        # ans = 0
        # t = x ^ y
        # while t:
        #     t = t & (t - 1)  # this operation in fact removes the last 1 bit from t
        #     ans += 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(7, 15))
    print(s.hammingDistance(1, 4))
