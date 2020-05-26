class Solution:
    def findMaxLength(self, nums) -> int:
        d = {0: -1}
        ans = sum_list = 0
        for idx, num in enumerate(nums):
            if num == 1:
                sum_list += 1
            else:
                sum_list -= 1
            if sum_list in d:
                ans = max(ans, idx - d[sum_list])
            else:
                d[sum_list] = idx
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxLength([0, 1, 0]))
    print(s.findMaxLength([0, 1, 0, 1]))
