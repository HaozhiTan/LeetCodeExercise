class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        # 2 pointer
        start_point = 0
        end_point = 0
        m = 1
        ans = 0
        while end_point < len(nums):
            m *= nums[end_point]
            while end_point >= start_point and m >= k:
                m //= nums[start_point]
                start_point += 1
            # number of subarrays ending with end_point with product less than k
            ans += end_point - start_point + 1
            end_point += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
