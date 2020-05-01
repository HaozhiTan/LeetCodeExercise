import functools
import heapq

class Solution:
    def lastStoneWeight(self, stones) -> int:
        # if len(stones) == 1:
        #     return stones[0]
        # elif len(stones) == 2:
        #     return abs(stones[0] - stones[1])
        # else:
        #     while len(stones) > 1:
        #         stones = sorted(stones, reverse=True)
        #         stones = stones[2:] + [stones[0] - stones[1]]
        #     return stones[0]

        # return functools.reduce(lambda a, b: abs(a - b), stones)

        # priority heaps
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x1 = heapq.heappop(stones)
            x2 = heapq.heappop(stones)
            if x1 != x2:
                heapq.heappush(stones, -abs(x1-x2))
        if len(stones) == 0:
            return 0
        return -stones[0]


if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight([9, 7, 7, 6, 6]))
