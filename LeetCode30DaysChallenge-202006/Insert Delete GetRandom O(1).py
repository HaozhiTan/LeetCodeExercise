import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.nums_position = {}
        self.len = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.nums_position:
            return False
        else:
            self.nums.append(val)
            self.nums_position[val] = self.len
            self.len += 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.nums_position:
            return False
        else:
            pos = self.nums_position[val]
            self.nums[pos] = self.nums[-1]  # move to the end
            self.nums_position[self.nums[pos]] = pos  # update the position
            self.nums.pop()
            self.nums_position.pop(val)
            self.len -= 1
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, self.len-1)]


if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.insert(3))
    print(obj.remove(1))
    print(obj.remove(1))
    print(obj.insert(3))
    print(obj.getRandom())
    print(obj.getRandom())

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()