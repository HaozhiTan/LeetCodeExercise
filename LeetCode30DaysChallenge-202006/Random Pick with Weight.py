import random


class Solution:

    def __init__(self, w):
        self.weights = w
        self.size = len(w)

    def pickIndex(self) -> int:
        # random pick the index based on the weights, it is slow to use this function, but it's very intuitive
        return random.choices(range(self.size), weights=self.weights)[0]


if __name__ == '__main__':
    # s = Solution([1, 3])
    s = Solution([1])
    print(s.pickIndex())
    print(s.pickIndex())
    print(s.pickIndex())
    print(s.pickIndex())
    print(s.pickIndex())

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
