class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        count = 0
        for idx in range(nums_len):
            if nums[idx] != 0:
                nums[count] = nums[idx]
                count = count + 1

        for idx in range(count, nums_len):
            nums[idx] = 0


if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0, 1, 0, 3, 12])
