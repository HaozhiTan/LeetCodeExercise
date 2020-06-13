class Solution:
    def largestDivisibleSubset(self, nums):
        # dp
        if not nums:
            return []
        nums_len = len(nums)
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(0, nums_len-1):
            for j in range(i+1, nums_len):
                if nums[j] % nums[i] == 0 and len(dp[j]) < len(dp[i])+1:
                    dp[j] = dp[i] + [nums[j]]
        return max(dp, key=len)


if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([1, 2, 3, 4]))