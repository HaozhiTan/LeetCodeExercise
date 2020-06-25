class Solution:
    def findDuplicate(self, nums) -> int:
        # Floyd's Tortoise and Hare (Cycle Detection)
        tortoise = hare = nums[0]
        # find the first intersection point
        while True:
            tortoise = nums[nums[tortoise]]
            hare = nums[hare]
            if tortoise == hare:
                break
        # move tortoise to the start_point, and keep two at same speed
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))
    print(s.findDuplicate([1, 3, 4, 4, 4]))
