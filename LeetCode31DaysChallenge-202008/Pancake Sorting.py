class Solution:
    def pancakeSort(self, A):
        # start from the largest number to flip to the beginning first and then flip last.
        ans = []
        len_list = len(A)
        for num in range(len_list, 0, -1):
            idx = A.index(num)
            if idx == num - 1:
                continue
            elif idx != 0:
                ans.append(idx + 1)
                A[:idx + 1] = A[:idx + 1][::-1]
            ans.append(num)
            A[:num] = A[:num][::-1]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.pancakeSort([3, 2, 4, 1]))
    print(s.pancakeSort([1, 2, 3]))
