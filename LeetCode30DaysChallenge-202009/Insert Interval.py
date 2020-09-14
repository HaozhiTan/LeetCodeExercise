class Solution:
    def insert(self, intervals, newInterval):
        # no intervals
        if not intervals:
            return [newInterval]
        # insert at the beginning:
        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals

        # insert at the end:
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]

        # insert in the middle but no merging:
        for idx in range(1, len(intervals)):
            if intervals[idx - 1][1] < newInterval[0] < intervals[idx][0] and newInterval[1] < intervals[idx][0]:
                return intervals[:idx] + [newInterval] + intervals[idx:]

        start_index = 0
        end_index = len(intervals) - 1
        # insert in the middle with merging:
        for idx, interval in enumerate(intervals):
            if interval[0] <= newInterval[0] <= interval[1]:
                start_index = idx
                break
            elif idx > 0 and intervals[idx - 1][1] < newInterval[0] < intervals[idx][0]:
                start_index = idx
                break
        for idx, interval in enumerate(intervals):
            if interval[0] <= newInterval[1] <= interval[1]:
                end_index = idx
                break
            elif idx > 0 and intervals[idx - 1][1] < newInterval[1] < intervals[idx][0]:
                end_index = idx - 1
                break
        ans = intervals[:start_index] + [
            [min(intervals[start_index][0], newInterval[0]), max(newInterval[1], intervals[end_index][1])]] + intervals[
                                                                                                              end_index + 1:]
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.insert(intervals=[], newInterval=[5, 7]))
    # print(s.insert(intervals=[[1, 5]], newInterval=[0, 0]))
    # print(s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    # print(s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
    # print(s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[0, 1]))
    # print(s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[16, 18]))
    # print(s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[1, 18]))
    # print(s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[2, 11]))
    print(s.insert([[0, 5], [9, 12]], [7, 16]))
