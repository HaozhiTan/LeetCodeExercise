class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        # minutes degree
        minutes_degree = minutes / 60 * 360
        # hours degree without considering minutes
        hours_degree = 360 // 12 * hour
        # add the minutes effect to hours
        hours_degree += 360 // 12 * minutes / 60
        # difference
        d = abs(hours_degree - minutes_degree)
        if d > 180:
            return 360 - d
        else:
            return d


if __name__ == '__main__':
    s = Solution()
    print(s.angleClock(12, 30))
    print(s.angleClock(3, 30))
    print(s.angleClock(3, 15))
    print(s.angleClock(4, 50))
    print(s.angleClock(12, 0))

