from itertools import combinations


class Solution:
    def subsets(self, nums):
        # # intuitive way
        # ans = []
        # for i in range(len(nums) + 1):
        #     ans += list(map(list, combinations(nums, i)))
        # return ans
        # bitmask
        ans = []
        n = len(nums)
        for i in range(2 ** n, 2 ** (n + 1)):
            # get from 00...0 to 11...1
            bitmask = bin(i)[3:]
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
