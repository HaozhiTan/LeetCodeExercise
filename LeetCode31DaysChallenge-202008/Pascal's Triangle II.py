class Solution:
    def getRow(self, rowIndex: int):
        prev = [1]
        current_row = 0
        while current_row < rowIndex:
            current = [1]
            for idx in range(len(prev) - 1):
                current.append(prev[idx] + prev[idx + 1])
            current.append(1)
            current_row += 1
            prev = current.copy()
        return prev


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(0))
    print(s.getRow(1))
    print(s.getRow(2))
    print(s.getRow(3))
    print(s.getRow(10))
    print(s.getRow(4))


