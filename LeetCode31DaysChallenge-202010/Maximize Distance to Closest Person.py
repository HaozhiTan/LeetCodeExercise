from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ones_index = [index for index, seat in enumerate(seats) if seat == 1]
        ans = 0
        if ones_index[0] > 0:
            ans = max(ans, ones_index[0])
        if ones_index[-1] < len(seats) - 1:
            ans = max(ans, len(seats) - 1 - ones_index[-1])
        if len(ones_index) >= 2:
            index_diff = [ones_index[i] - ones_index[i - 1] for i in range(1, len(ones_index))]
            for diff in index_diff:
                ans = max(ans, diff // 2)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
    print(s.maxDistToClosest([0, 0, 0, 0, 1, 0, 1]))
    print(s.maxDistToClosest([1, 0, 0, 0]))
    print(s.maxDistToClosest([0, 1]))
    print(s.maxDistToClosest([1, 0]))
    print(s.maxDistToClosest([1, 0, 1, 0, 1, 0, 1]))