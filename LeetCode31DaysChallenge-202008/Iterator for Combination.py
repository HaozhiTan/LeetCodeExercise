from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = list(combinations(characters, combinationLength))
        self.curr_idx = -1
        self.length = len(self.combs)

    def next(self) -> str:
        self.curr_idx += 1
        return ''.join(self.combs[self.curr_idx])

    def hasNext(self) -> bool:
        if (self.curr_idx + 1) < self.length:
            return True
        else:
            return False


if __name__ == '__main__':
    # Your CombinationIterator object will be instantiated and called as such:
    obj = CombinationIterator("abc", 2)
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()