from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        ans = 0
        sum = 0
        d = defaultdict(int)
        d[0] += 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in d.keys():
                ans += d[sum-k]
            d[sum] += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1,1,1], 2))
    print(s.subarraySum([1,1,11], 11))
    print(s.subarraySum([1,11,11], 23))
    print(s.subarraySum([1,2], 23))
    print(s.subarraySum([1,2,1,2,1], 3))
