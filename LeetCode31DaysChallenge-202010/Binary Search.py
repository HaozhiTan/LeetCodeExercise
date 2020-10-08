from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=8))
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=123))
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=-2))