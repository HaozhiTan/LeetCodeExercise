# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # self.ans = 0
        # def find(left, right):
        #     if left > right or self.ans > 0:
        #         return
        #     mid = (left + right) // 2
        #     if not isBadVersion(mid):
        #         find(mid+1, right)
        #     else:
        #         if not isBadVersion(mid-1):
        #             self.ans = mid
        #             return
        #         find(left, mid)
        # find(1, n)
        # return self.ans
        ans = 0
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans

