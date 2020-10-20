from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        s, n = {1, 2, 3, 4, 5, 6}, len(A)
        for i in range(n):
            s &= {A[i], B[i]}
        if not s:
            return -1
        flips1 = sum(A[i] == list(s)[0] for i in range(n))
        flips2 = sum(B[i] == list(s)[0] for i in range(n))
        return min(n - flips1, n - flips2)
