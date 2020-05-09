class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # # binary search
        # left = 1
        # right = num
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * mid == num:
        #         return True
        #     elif mid * mid > num:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False

        # power same speed with binary search
        k = num ** 0.5
        return k == int(k)


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(14))
    print(s.isPerfectSquare(1))
    print(s.isPerfectSquare(2))
    print(s.isPerfectSquare(3))
    print(s.isPerfectSquare(4))
    print(s.isPerfectSquare(16))
    print(s.isPerfectSquare(1232132189471))
    print(s.isPerfectSquare(1232132189471**2))
