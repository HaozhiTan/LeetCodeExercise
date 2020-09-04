class Solution:
    def partitionLabels(self, S: str):
        # greedy algorithm
        ans = []
        max_needed_idx = 0
        for idx, c in enumerate(S):
            needed_idx = S.rfind(c)
            max_needed_idx = max(needed_idx, max_needed_idx)
            if idx >= max_needed_idx:
                ans.append(idx + 1 - sum(ans))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
    print(s.partitionLabels("abaccbdeffed"))
    print(s.partitionLabels("abc"))
