class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N != 0:
            return (1 << N.bit_length()) - 1 - N
        else:
            return 1
