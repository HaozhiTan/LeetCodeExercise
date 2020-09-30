class Solution:
    def firstMissingPositive(self, nums) -> int:
        if len(nums) == 0:
            return 1
        # for i in range(1, len(nums) + 2):
        #     if i not in nums:
        #         return i
        # to use O(n) time and O(1) space
        # make the number as negative when met
        for idx in range(len(nums)):
            if nums[idx] <= 0 or nums[idx] > len(nums):
                nums[idx] = len(nums) + 1
        for num in nums:
            value = abs(num)
            if value <= len(nums):
                nums[value - 1] = -abs(nums[value - 1])
        for idx in range(len(nums)):
            if nums[idx] >= 0:
                return idx + 1
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([3, 4, -1, 1]))
