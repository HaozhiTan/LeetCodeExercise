import bisect
# This module provides support for maintaining a list in sorted order without having to sort the list after each insertion


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # binary search
        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if target == nums[mid]:
        #         return mid
        #     elif target > nums[mid]:
        #         left = mid + 1
        #     elif target < nums[mid]:
        #         right = mid - 1
        # return left

        # bisect module (very fast)
        bisect.insort(nums, target)
        return nums.index(target)


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 2, 3, 4], 3))
    print(s.searchInsert([1, 2, 4, 5], 3))
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3, 5, 6], 7))
    print(s.searchInsert([1, 3, 5, 6], 0))
    print(s.searchInsert([1, 3, 5, 6], 4))
