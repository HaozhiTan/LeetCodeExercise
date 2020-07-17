from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        frequency = Counter(nums)
        return [num[0] for num in frequency.most_common(k)]
        # return heapq.nlargest(k, frequency.keys(), key=frequency.get)


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1], 1))
