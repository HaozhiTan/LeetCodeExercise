class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        max_candies = max(candies)
        return map(lambda x: x + extraCandies >= max_candies, candies)


if __name__ == '__main__':
    s = Solution()
    print(s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
