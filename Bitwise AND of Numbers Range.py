import functools

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if n < m * 2:
            nums = range(m, n+1)
            ans = functools.reduce(lambda a, b : a & b, nums)
        else:
            ans = 0
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(5, 7))
    print(s.rangeBitwiseAnd(0, 1))
    print(s.rangeBitwiseAnd(1, 2147483647))
