class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        # maximum non-empty subarray sum
        def kadane(nums):
            ans = curr = float('-inf')
            for num in nums:
                curr = num + max(curr, 0)
                ans = max(ans, curr)
            return ans

        # non-circular
        ans1 = kadane(A)

        sum_A = sum(A)
        ans2 = sum_A + kadane([-A[i] for i in range(1, len(A))])

        ans3 = sum_A + kadane([-A[i] for i in range(len(A) - 1)])

        return max(ans1, ans2, ans3)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([5, -3, 5]))
