class Solution:
    def hIndex(self, citations) -> int:
        # O(n)
        l = len(citations)
        lst = [0] * (l + 1)
        for num in citations:
            if num < l:
                lst[num] += 1
            else:
                lst[l] += 1
        total = 0
        for i in range(l, -1, -1):
            total += lst[i]
            if total >= i:
                return i


if __name__ == '__main__':
    s = Solution()
    # print(s.hIndex([3, 0, 6, 1, 5]))
    print(s.hIndex([4, 0, 6, 1, 5]))
