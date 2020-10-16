from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for row and column
        if not matrix or not matrix[0]:
            return False
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, rows - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] == target:
                return True
            else:
                right = mid - 1
        row = right
        if row < 0 or row >= rows:
            return False
        left, right = 0, columns - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] == target:
                return True
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=13))
