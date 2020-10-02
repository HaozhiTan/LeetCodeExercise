from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def dfs(idx, num_list, num_sum):
            if num_sum == target:
                if num_list:
                    self.ans.append(num_list)
                return
            if num_sum > target:
                return
            for i in range(idx, len(candidates)):
                dfs(i, num_list + [candidates[i]], num_sum + candidates[i])
            return

        dfs(0, [], 0)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))
    print(s.combinationSum(candidates=[2, 3, 5], target=8))
