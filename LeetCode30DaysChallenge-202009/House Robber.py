class Solution:
    def rob(self, nums) -> int:
        # dp
        if not nums:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx + 1] = max(dp[idx], dp[idx - 1] + nums[idx])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
