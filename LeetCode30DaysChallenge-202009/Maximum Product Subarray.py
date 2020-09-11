class Solution:
    def maxProduct(self, nums) -> int:
        # dp_max[i] to store maximum value
        # dp_min[i] to store minimum value
        if not nums:
            return 0
        dp_max = [nums[0]]
        dp_min = [nums[0]]
        ans = dp_max[0]
        for i in range(1, len(nums)):
            dp_max.append(max(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i]))
            dp_min.append(min(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i]))
            ans = max(dp_max[-1], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-2, 0, -1]))
    print(s.maxProduct([-1, -2, -3, -4, 2, 3, -2, -4]))
    print(s.maxProduct([2, 3, -1, -4]))
    print(s.maxProduct([2, 3, -2, 4]))
