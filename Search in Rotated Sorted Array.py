class Solution:
    def search(self, nums, target) -> int:
        def find(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if target <= nums[mid] and target >= nums[left]:
                    return find(left, mid)
                else:
                    return find(mid+1, right)
            if nums[mid+1] <= nums[right]:
                if target >= nums[mid+1] and target <= nums[right]:
                    return find(mid+1, right)
                else:
                    return find(left, mid)
        return find(0, len(nums)-1)

if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 3))
    print(s.search([4,5,6,7,0,1,2], 2))
    print(s.search([4,5,6,7,0,1,2], 7))
