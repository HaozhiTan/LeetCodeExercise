class Solution:
    def countBits(self, num: int):
        # 0
        # 1
        # 1 2 (0 -> 1, 1 -> 2)
        # 1 2 2 3 (0 -> 1, 1 -> 2, 1 -> 2, 2 -> 3)
        ans = [0]
        count = offset = 1
        for i in range(1, num+1):
            ans.append(ans[i-offset]+1)
            count -= 1
            if count == 0:
                offset *= 2
                count = offset
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(100))

