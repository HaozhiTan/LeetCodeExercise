class Solution:
    def productExceptSelf(self, nums):
        nums_len = len(nums)
        ans = [1]
        for i in range(1, nums_len):
            ans.append(ans[i-1] * nums[i-1])
        r = 1
        for i in range(nums_len-2, -1, -1):
            r = r * nums[i+1]
            ans[i] = ans[i] * r
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([1, 1, 1, 1, 2, 2, 2, 2]))
