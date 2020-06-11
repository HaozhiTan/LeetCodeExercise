class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # two pointer algorithm
        # left = 0
        # right = len(nums) - 1
        # for idx, num in enumerate(nums):
        #     if num == 0 and idx > left:
        #         while left < idx and nums[left] == 0:
        #             left += 1
        #         if left < idx:
        #             nums[left], nums[idx] = nums[idx], nums[left]
        #             left += 1
        #     elif num == 2 and idx < right:
        #         while right > idx and nums[right] == 2:
        #             right -= 1
        #         if right > idx:
        #             nums[right], nums[idx] = nums[idx], nums[right]
        #             right -= 1
        #             if nums[idx] == 0 and idx > left:
        #                 while left < idx and nums[left] == 0:
        #                     left += 1
        #                 if left < idx:
        #                     nums[left], nums[idx] = nums[idx], nums[left]
        #                     left += 1
        # return nums
        # three pointer algorithms
        left = 0  # track 0
        mid = 0  # track 1
        right = len(nums) - 1  # track 2
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
            elif nums[mid] == 1:
                mid += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([2, 0, 2, 1, 1, 0]))
    print(s.sortColors([2, 1, 2, 1, 1, 1]))
    print(s.sortColors([2, 2, 2, 2, 2, 2]))
    print(s.sortColors([1, 2, 0]))
