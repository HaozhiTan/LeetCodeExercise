import collections


class Solution:
    def threeSum(self, nums):
        counter = collections.Counter(nums)
        nums = sorted(counter)
        ans = []
        for idx, num in enumerate(nums):
            # 1.three numbers are same
            if num == 0 and counter[num] >= 3:
                ans.append([num, num, num])
            # 2. two numbers are same
            elif counter[num] >= 2 and -2 * num in counter and -2 * num != num:
                ans.append([num, num, -2 * num])
            # 3. three numbers are all different
            if num >= 0:
                continue
            if idx < len(nums) - 1 and nums[idx] + nums[idx + 1] >= 0:
                continue
            sums_to_get = -num
            # This part could use binary search to improve the performance
            for i in range(idx + 1, len(nums)):
                if nums[i] > sums_to_get // 2:
                    break
                nums_to_search = sums_to_get - nums[i]
                if nums_to_search in counter and nums_to_search != nums[i]:
                    ans.append([num, nums[i], nums_to_search])
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(s.threeSum(
    #     [0, 0, 0, -1, -1, -1, -2, -2, -2, 1, 1, 1, 2, 2, 2, 3, 1, 2, 3, 4, 1, 2, 2, 3, 4, 5, 1, 2, 2, 3, 4, 5, 5, -1,
    #      -5, -3, -4, -5]))
    print(s.threeSum([0, 0]))
