class Solution:
    def findMaxLength(self, nums) -> int:
        lookup = {0: -1}
        ans = 0
        count = 0
        for idx, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in lookup:
                ans = max(ans, idx - lookup[count])
            else:
                lookup[count] = idx
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxLength([0, 1, 0]))
