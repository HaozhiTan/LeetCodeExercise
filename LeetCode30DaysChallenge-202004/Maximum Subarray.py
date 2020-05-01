class Solution:
    def maxSubArray(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        return max(self.maxSubArray(nums[left:mid+1]), self.maxSubArray(nums[mid+1:right+1]), self.maxCrossSum(nums))

    def maxCrossSum(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        left_sum = -float("inf")
        current_sum = 0
        for i in range(mid, left-1, -1):
            current_sum = current_sum + nums[i]
            if current_sum > left_sum:
                left_sum = current_sum
        right_sum = -float("inf")
        current_sum = 0
        for i in range(mid+1, right+1):
            current_sum = current_sum + nums[i]
            if current_sum > right_sum:
                right_sum = current_sum
        return left_sum + right_sum


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
