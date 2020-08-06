class Solution:
    def findDuplicates(self, nums):
        # rearrange number to use the properties that 1 ≤ a[i] ≤ n (n = size of array)
        idx = 0
        while idx < len(nums):
            while nums[idx] != idx + 1:
                if nums[idx] == nums[nums[idx] - 1]:
                    break
                else:
                    temp = nums[idx] - 1
                    nums[idx], nums[temp] = nums[temp], nums[idx]
            idx += 1
        return [num for idx, num in enumerate(nums) if num != idx + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.findDuplicates([4, 3, 2, 7, 4, 2, 3, 7]))

