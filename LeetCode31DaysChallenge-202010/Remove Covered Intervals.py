from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda lst: (lst[0], -lst[1]))
        removes = 0
        last_interval = intervals[0][1]
        for interval in intervals[1:]:
            if interval[1] <= last_interval:
                removes += 1
            else:
                last_interval = interval[1]
        return len(intervals) - removes


if __name__ == '__main__':
    s = Solution()
    print(s.removeCoveredIntervals(intervals=[[3, 10], [4, 10], [5, 11]]))
