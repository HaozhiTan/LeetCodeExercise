from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums) -> str:
        larger_number = lambda a,b : 1 if a + b > b + a else -1 if a + b < b + a else 0
        nums = map(str, nums)
        ans = ''.join(sorted(map(str, nums), key=cmp_to_key(larger_number), reverse=True))
        if ans[0] == '0':
            return '0'
        else:
            return ans


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([10, 2]))
    print(s.largestNumber([3, 30, 34, 5, 9]))
