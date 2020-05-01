class Solution:
    def singleNumber(self, nums) -> int:
        # nums = sorted(nums)
        # ans = nums[0]
        # for idx in range(1, len(nums)):
        #     if idx != len(nums)-1:
        #         if (nums[idx] != nums[idx-1]) and (nums[idx] != nums[idx+1]):
        #             ans = nums[idx]
        #             break
        #     else:
        #         if nums[idx] != nums[idx-1]:
        #             ans = nums[idx]
        # return ans
        """Math: 2*(a+b+c) - (a+a+b+b+c) = c"""
        sum_list = sum(nums)
        double_sum = sum(set(nums)) * 2
        return double_sum - sum_list


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1, 2, 2]))

