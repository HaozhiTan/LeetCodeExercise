class Solution:
    def singleNumber(self, nums) -> int:
        # math 3*(a+b+c) - (3a+3b+c) = 2*c
        return (3 * sum(set(nums)) - sum(nums)) // 2


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))

