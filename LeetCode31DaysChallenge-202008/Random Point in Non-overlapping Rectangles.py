import bisect
import itertools
import random
import functools


class Solution:

    def __init__(self, rects):
        self.rect_areas = [(rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) for rect in rects]
        self.weights = [area / sum(self.rect_areas) for area in itertools.accumulate(self.rect_areas)]
        self.rects = rects

    def pick(self):
        rect_idx = bisect.bisect(self.weights, random.random())
        rect = self.rects[rect_idx]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]


if __name__ == '__main__':
    s = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
    # print(s.pick())
    # print(s.pick())
    # print(s.pick())
    # print(s.pick())
    # print(s.pick())
    # print(s.pick())
    # print(s.pick())
    # print(s.pick())

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
