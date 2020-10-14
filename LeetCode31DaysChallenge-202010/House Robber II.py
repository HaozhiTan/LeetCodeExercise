from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # max(dp[0:n-2], dp[1:n-1])
        if len(nums) <= 3:
            return max(nums)

        def dynamic_programming(num_list):
            dp = [0] * (len(num_list) + 1)
            dp[1] = num_list[0]
            for idx in range(1, len(num_list)):
                dp[idx + 1] = max(dp[idx - 1] + num_list[idx], dp[idx])
            return dp[-1]

        return max(dynamic_programming(nums[:len(nums) - 1]), dynamic_programming(nums[1:len(nums)]))


if __name__ == '__main__':
    s = Solution()
    print(s.rob(nums=[1, 2, 3, 1]))
