# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(self.matrix)
        if self.row == 0:
            self.column = 0
        else:
            self.column = len(self.matrix[0])

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def dimensions(self):
        return [self.row, self.column]

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions = binaryMatrix.dimensions()
        self.rows = dimensions[0]
        self.columns = dimensions[1]
        ans = -1
        start_row = 0
        start_column = self.columns - 1
        while start_row < self.rows and start_column >= 0:
            if binaryMatrix.get(start_row, start_column) == 0:
                start_row += 1
            else:
                ans = start_column
                start_column -= 1
        return ans



if __name__ == "__main__":
    s = Solution()
    m1 = BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])
    print(s.leftMostColumnWithOne(m1))
    m2 = BinaryMatrix([[0,0],[0,0]])
    print(s.leftMostColumnWithOne(m2))