class Solution:
    def intervalIntersection(self, A, B):
        # intuitive
        len_a = len(A)
        len_b = len(B)
        point_a = point_b = 0
        ans = []
        while point_a < len_a and point_b < len_b:
            if A[point_a][1] <= B[point_b][1]:
                if A[point_a][0] <= B[point_b][0]:
                    if A[point_a][1] >= B[point_b][0]:
                        ans.append([B[point_b][0], A[point_a][1]])
                else:
                    ans.append([A[point_a][0], A[point_a][1]])
                point_a += 1
            else:
                if A[point_a][0] <= B[point_b][0]:
                    ans.append([B[point_b][0], B[point_b][1]])
                else:
                    if B[point_b][1] >= A[point_a][0]:
                        ans.append([A[point_a][0], B[point_b][1]])
                point_b += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))

