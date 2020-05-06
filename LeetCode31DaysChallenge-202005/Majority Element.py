class Solution:
    def majorityElement(self, nums) -> int:
        # O(n)
        length = len(nums)
        s_nums = set(nums)
        for i in s_nums:
            if nums.count(i) > length // 2:
                return i

        # # sort O(nlogn)
        # nums.sort()
        # return nums[len(nums)//2]

        # # Boyer-Moore Voting Algorithm O(n)
        # count = 0
        # for i in nums:
        #     if count == 0:
        #         candidate = i
        #     if candidate == i:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
