class Solution:
    def sortArrayByParity(self, A):
        # O(n) two pointer
        head = 0
        tail = len(A) - 1
        while head < tail:
            if A[head] % 2 == 1: # odd element
                while A[tail] % 2 == 1 and tail > head:
                    tail -= 1
                A[head], A[tail] = A[tail], A[head]
            else:
                head += 1
        return A


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4, 2, 3, 4, 5, 6, 7, 8]))

