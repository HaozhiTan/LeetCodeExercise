class Solution:
    def combinationSum3(self, k: int, n: int):
        def dfs(last_num, current_sum, num_list):
            if len(num_list) == k and current_sum == n:
                self.ans.append(num_list)
                return
            if current_sum >= n or len(num_list) >= k:
                return
            for i in range(last_num + 1, 10):
                dfs(i, current_sum+i, num_list + [i])
            return
        self.ans = []
        dfs(0, 0, [])
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))