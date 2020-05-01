class Solution:
    def canJump(self, nums) -> bool:
        # O(n^2) Dynamic Programming
        # f = [False] * len(nums)
        # f[0] = True
        # for i in range(1, len(nums)):
        #     for j in range(i-1, -1, -1):
        #         if f[j] and (j + nums[j]) >= i:
        #             f[i] = True
        #             break
        # return f[-1] 

        # O(n) Greedy
        last_position = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        return last_position == 0

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
    
