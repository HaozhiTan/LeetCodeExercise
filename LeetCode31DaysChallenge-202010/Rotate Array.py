from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # cyclic replacement
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, previous = start, nums[start]
            while True:
                next_index = (current + k) % n
                previous, nums[next_index] = nums[next_index], previous
                current = next_index
                count += 1

                if start == current:
                    break
            start += 1

