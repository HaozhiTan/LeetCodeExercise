class Solution:
    def numsSameConsecDiff(self, N: int, K: int):
        # dfs or bfs
        def recursive(curr_len, num):
            if curr_len == N:
                self.ans.append(int(num))
                return
            temp_num = int(num[curr_len - 1])
            if temp_num - K >= 0:
                recursive(curr_len + 1, num + str(temp_num - K))
            if 10 > temp_num + K != temp_num - K:
                recursive(curr_len + 1, num + str(temp_num + K))
            return
        if N == 1:
            return list(range(10))
        self.ans = []
        for i in range(1, 10):
            recursive(1, str(i))
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.numsSameConsecDiff(1, 2))
    print(s.numsSameConsecDiff(3, 7))
    print(s.numsSameConsecDiff(2, 1))
    print(s.numsSameConsecDiff(2, 0))
