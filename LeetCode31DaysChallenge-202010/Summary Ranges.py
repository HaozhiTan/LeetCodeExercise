class Solution:
    def summaryRanges(self, nums):
        # two pointer
        i, N = 0, len(nums)
        ans = []

        while i < N:
            beg = end = i
            while end < N - 1 and nums[end] + 1 == nums[end + 1]:
                end += 1
            ans.append(str(nums[beg]) + ("->" + str(nums[end])) * (beg != end))
            i = end + 1

        return ans