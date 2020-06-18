class Solution:
    def hIndex(self, citations) -> int:
        left = 0
        right = len(citations) - 1
        if not any(citations):
            return 0
        while left <= right:
            mid = (left + right) // 2
            if len(citations) - mid <= citations[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([0, 1, 3, 5, 6]))
    print(s.hIndex([0, 1, 4, 5, 6]))
    print(s.hIndex([0, 5, 11, 13, 14, 15]))
    print(s.hIndex([6, 10, 11, 13, 14, 15]))
    print(s.hIndex([0]))
    print(s.hIndex([0, 0]))
