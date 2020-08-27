import bisect


class Solution:
    def findRightInterval(self, intervals):
        # sorting and binary search to find the ans
        intervals_list = sorted([[start_i, end_i, idx] for idx, [start_i, end_i] in enumerate(intervals)])
        binary_search_list = [start_i for start_i, _, _ in intervals_list]
        ans = [-1] * len(intervals)
        for start_i, end_i, idx in intervals_list:
            t = bisect.bisect_left(binary_search_list, end_i)
            if t < len(binary_search_list):
                ans[idx] = intervals_list[t][2]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findRightInterval([[1, 4], [2, 3], [3, 4]]))

