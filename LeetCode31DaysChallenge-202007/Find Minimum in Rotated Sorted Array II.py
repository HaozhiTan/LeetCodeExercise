class Solution:
    def findMin(self, nums) -> int:
        # return min(nums)
        # binary search + dfs
        def dfs(left, right):
            if right - left <= 1:
                self.ans = min(self.ans, nums[left], nums[right])
                return
            mid = (left + right) // 2
            if nums[mid] >= nums[right]:
                dfs(mid + 1, right)
            if nums[mid] <= nums[right]:
                dfs(left, mid)

        self.ans = float('inf')
        dfs(0, len(nums)-1)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([10, 1, 10, 10, 10]))
    print(s.findMin([1, 3, 5]))
    print(s.findMin([2, 2, 2, 0, 1]))
    print(s.findMin([2, 2, 2, 0, 1, 2]))
    print(s.findMin([2, 2, 2]))
    print(s.findMin([2, 2, 2, 2, 1]))
