class Solution:
    def findJudge(self, N: int, trust) -> int:
        flag = [0] * (N + 1)
        for (a, b) in trust:
            flag[a] -= 1
            flag[b] += 1
        ans = -1
        for i in range(1, N + 1):
            if flag[i] == N - 1:
                return i
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
    print(s.findJudge(N=3, trust=[[1, 2], [2, 3]]))
    print(s.findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))
    print(s.findJudge(N=2, trust=[[1, 2]]))
