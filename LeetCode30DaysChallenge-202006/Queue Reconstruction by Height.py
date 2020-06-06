class Solution:
    def reconstructQueue(self, people):
        # # sort the height in the descending order (fast)
        # # if height is same, sort the k in ascending order
        # people.sort(key=lambda lst: (-lst[0], lst[1]))
        # ans = []
        # for p in people:
        #     ans.insert(p[1], p)
        # return ans
        # sort the height in the ascending order (slow)
        # if height is same, sort the k in ascending order
        people.sort(key=lambda lst: (lst[0], lst[1]))
        length = len(people)
        ans = [None] * length
        for p in people:
            target = p[1]
            current_index = 0
            while target > 0:
                if ans[current_index] is None or ans[current_index][0] >= p[0]:
                    target -= 1
                current_index += 1
            while ans[current_index] is not None:
                current_index += 1
            ans[current_index] = p
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

