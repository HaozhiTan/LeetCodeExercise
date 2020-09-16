class Solution:
    def findMaximumXOR(self, nums) -> int:
        ans = 0
        for i in range(31, -1, -1):
            # get the prefix
            nums_prefix = set([num >> i for num in nums])
            ans <<= 1  # 0 -> 00 1 ->10
            candidate = ans + 1  # 0->01 1->11
            for prefix in nums_prefix:
                if candidate ^ prefix in nums_prefix:
                    ans = candidate
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))
