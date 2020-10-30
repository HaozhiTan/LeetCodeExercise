import bisect
from typing import List
import sys


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # # O(n^2)
        # if not nums:
        #     return 0
        # dp = [1] * len(nums)  # the length of the longest increasing sequence ends at index i
        # ans = [1] * len(nums)  # count of such longest increasing sequence
        # longest_seq = 0
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             if dp[j] + 1 == dp[i]:
        #                 ans[i] += ans[j]
        #             elif dp[j] + 1 > dp[i]:
        #                 ans[i] = ans[j]
        #                 dp[i] = dp[j] + 1
        #     longest_seq = max(longest_seq, dp[i])
        #
        # return sum([ans[i] for i in range(len(nums)) if dp[i] == longest_seq])
        # O(nlogn)
        if not nums:
            return 0
        n = len(nums) + 1

        decks, ends_decks, paths = [[] for _ in range(n)], [sys.maxsize] * n, [[0] for _ in range(n)]
        for num in nums:
            idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            if idx > 0:
                l = bisect.bisect(decks[idx - 1], -num)
                n_paths = paths[idx - 1][-1] - paths[idx - 1][l]

            decks[idx].append(-num)
            ends_decks[idx] = num
            paths[idx].append(n_paths + paths[idx][-1])

        return paths[paths.index([0]) - 1][-1]
