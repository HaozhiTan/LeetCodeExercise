from collections import Counter


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        # The most frequent character will be placed at (n+1)th distance from each other,
        # such that the gap between them remains 'n'. So, max_freq will count the maximum occurence of the character.
        # Finally, minimum time idle_time will be (max_freq-1)*(n+1)+1,
        # +1 because at the last occurence of the element we must stop.
        # This minimum required time can be extended if there are same number of maximum frequency elements in the character array,
        # here, denoted by inc, so +1 for all such elements. Now, if the other char does not fit in this time we must consider the complete tasks.size().
        d = list(Counter(tasks).values())  # This cannot garantee the descending order
        return max((max(d) - 1) * (n + 1) + 1 + d.count(max(d)) - 1, len(tasks))


if __name__ == '__main__':
    s = Solution()
    print(s.leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
    print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))

