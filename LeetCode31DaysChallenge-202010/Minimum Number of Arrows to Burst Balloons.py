from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Greedy
        points.sort(key=lambda a: a[1])
        ans = 1
        if len(points) == 0:
            return 0
        current_point = points[0]
        for i in range(len(points)):
            if points[i][0] > current_point[1]:
                ans += 1
                current_point = points[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
