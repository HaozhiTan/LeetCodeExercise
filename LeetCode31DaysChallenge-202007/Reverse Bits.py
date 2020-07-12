class Solution:
    def reverseBits(self, n: int) -> int:
        # # use binary format
        # x = bin(n)
        # prefix = x[0:2]
        # num = x[2:]
        # length = len(num)
        # num = '0' * (32 - length) + num
        # num = num[::-1]
        # return int(prefix + num, 2)
        # use bit operation
        ans = 0
        for i in range(32):
            ans = (ans << 1) ^ (n & 1)  # add the last bit of the n to ans
            n >>= 1  # remove the last bit from n
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))

