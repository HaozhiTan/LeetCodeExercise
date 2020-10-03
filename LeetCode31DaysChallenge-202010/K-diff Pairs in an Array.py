from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_dict = Counter(nums)
        if k == 0:
            return sum([num_dict[key] > 1 for key in num_dict])
        else:
            return sum([(key + k) in num_dict for key in num_dict])


if __name__ == '__main__':
    s = Solution()
    print(s.findPairs(nums=[1, 2, 3, 4, 5], k=1))
