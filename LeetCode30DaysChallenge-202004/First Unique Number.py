import collections
# class Node:

#     def __init__(self, val):
#         self.value = val
#         self.next = None


class FirstUnique:

    def __init__(self, nums):
        self.d = collections.defaultdict(int)
        self.nums = []
        self.header = 0
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while (self.header < len(self.nums)) and (self.d[self.nums[self.header]] >= 2):
            self.header += 1
        if self.header >= len(self.nums) or len(self.nums) == 0:
            return -1
        else:
            return self.nums[self.header]

    def add(self, value: int) -> None:
        self.d[value] += 1
        if self.d[value] == 1:
            self.nums.append(value)

            
if __name__ == "__main__":
    firstUnique = FirstUnique([7,7,7,7,7,7])
    print(firstUnique.showFirstUnique())
    firstUnique.add(7)
    firstUnique.add(3)
    firstUnique.add(3)
    firstUnique.add(7)
    firstUnique.add(17)
    print(firstUnique.showFirstUnique())

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)