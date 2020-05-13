class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # intuitive way, delete the most large number from the left side
        if k >= len(num):
            return '0'
        elif k == 0:
            return str(int(num))
        else:
            ans = []
            for n in num:
                while ans and k > 0 and ans[-1] > n:
                    ans.pop()
                    k -= 1
                ans.append(n)
            if k != 0:
                return str(int(''.join(ans[:-k])))
            else:
                return str(int(''.join(ans)))

        # # DP too slow
        # if k == len(num):
        #     return '0'
        # elif k == 0:
        #     return str(int(num))
        # else:
        #     k = len(num) - k
        #     # dp[i][j] refers to minimum number at length of i for the first j words
        #     dp = [[' ' for j in range(len(num)+1)] for i in range(k+1)]
        #     for length in range(1, k+1):
        #         for idx in range(length-1, len(num)):
        #             try:
        #                 a = int(dp[length][idx])
        #             except:
        #                 a = 999999999
        #             b = int(dp[length-1][idx]+num[idx])
        #             if a < b:
        #                 dp[length][idx + 1] = dp[length][idx]
        #             else:
        #                 dp[length][idx + 1] = dp[length-1][idx]+num[idx]
        #     return str(int(dp[k][len(num)]))


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits('10200', 1))
    print(s.removeKdigits('1432219', 3))
    print(s.removeKdigits('10200', 5))
    print(s.removeKdigits('10200', 0))
    print(s.removeKdigits('12345', 2))
