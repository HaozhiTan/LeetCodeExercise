from math import sqrt


class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        max_candies = int(sqrt(candies * 2))
        while max_candies * (max_candies + 1) // 2 <= candies:
            max_candies += 1
        max_candies -= 1
        candies_left = candies - max_candies * (max_candies + 1) // 2
        full_rounds = max_candies // num_people
        left_people = max_candies - num_people * full_rounds
        ans = [0] * num_people
        for idx in range(left_people):
            ans[idx] += (full_rounds + 1) * (idx + 1) + (full_rounds + 1) * full_rounds * num_people // 2
        ans[left_people] += candies_left
        for idx in range(left_people, num_people):
            ans[idx] += full_rounds * (idx + 1) + full_rounds * (full_rounds - 1) * num_people // 2
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies(10, 3))
    print(s.distributeCandies(7, 4))

