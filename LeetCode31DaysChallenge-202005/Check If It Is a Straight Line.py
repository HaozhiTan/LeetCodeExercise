class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        # intuitive way
        if len(coordinates) <= 2:
            return True
        # try:
        #     k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        # except ZeroDivisionError:
        #     k = 0
        # b = coordinates[0][1] - k * coordinates[0][0]
        # for i in range(2, len(coordinates)):
        #     if coordinates[i][0] * k + b != coordinates[i][1]:
        #         return False
        # return True

        # (y2 - y1) / (x2 - x1) = (y - y1) / (x - x1) => (y2 - y1) * (x - x1) = (x2 - x1) * (y - y1)
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]
        for i in range(2, len(coordinates)):
            if (y2 - y1) * (coordinates[i][0] - x1) != (x2 - x1) * (coordinates[i][1] - y1):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
    print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(s.checkStraightLine([[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]]))
