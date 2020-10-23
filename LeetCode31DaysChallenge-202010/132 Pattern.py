from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        stack = []
        min_nums = [nums[0]]
        for i in range(1, len(nums)):
            min_nums.append(min(min_nums[i - 1], nums[i]))
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > min_nums[i]:
                while stack and stack[-1] <= min_nums[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.find132pattern([1, 2, 3, 4]))
    print(s.find132pattern([3, 1, 4, 2]))
    print(s.find132pattern([-1, 3, 2, 0]))
    print(s.find132pattern([4, 3, 2, 1]))
    print(s.find132pattern([1, 0, 1, -4, -3]))
