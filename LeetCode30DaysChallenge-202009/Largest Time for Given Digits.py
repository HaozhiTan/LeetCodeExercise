from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A) -> str:
        ans = ''
        list_A = permutations(A)
        for array in list_A:
            if (array[0] * 10 + array[1] < 24) and (array[2] * 10 + array[3] < 60):
                ans = max(ans, str(array[0]) + str(array[1]) + ":" + str(array[2]) + str(array[3]))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.largestTimeFromDigits([1, 2, 3, 4]))
    print(s.largestTimeFromDigits([4, 4, 3, 4]))
