from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        # Greedy
        tokens.sort()
        q = deque(tokens)
        scores = 0
        ans = 0
        while q and (P >= q[0] or scores > 0):
            while q and P >= q[0]:
                P -= q.popleft()
                scores += 1
            ans = max(ans, scores)
            if q and scores > 0:
                P += q.pop()
                scores -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.bagOfTokensScore(tokens=[100, 200, 300, 400], P=200))
