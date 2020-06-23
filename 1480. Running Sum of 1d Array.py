class Solution:
    def runningSum(self, nums):
        dp = []
        for idx, num in enumerate(nums):
            if idx == 0:
                dp.append(num)
            else:
                dp.append(num + dp[idx - 1])
        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.runningSum([3, 1, 2, 10, 1]))

