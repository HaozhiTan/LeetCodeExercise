class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        ans = 0
        to_poison_time = -1
        for idx, time in enumerate(timeSeries):
            if to_poison_time < time:
                ans += duration
            else:
                ans += time - timeSeries[idx - 1]
            to_poison_time = time + duration - 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findPoisonedDuration([1, 4], 2))
    print(s.findPoisonedDuration([1, 2, 3, 4, 5, 6, 7, 9, 10], 2))
