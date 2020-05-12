class Solution:
    def singleNonDuplicate(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 0 and nums[mid] == nums[mid+1]:
                left = mid + 2
            elif mid % 2 == 1 and nums[mid] == nums[mid-1]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
    print(s.singleNonDuplicate([3, 3, 7]))
    print(s.singleNonDuplicate([1, 3, 3, 7, 7]))
