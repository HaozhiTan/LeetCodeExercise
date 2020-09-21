class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        # bucket sort because we have the 0 <= trips[i][1] < trips[i][2] <= 1000
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]
        used_capacity = 0
        for time in timestamp:
            used_capacity += time
            if used_capacity > capacity:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11))
    print(s.carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3))
    print(s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))
