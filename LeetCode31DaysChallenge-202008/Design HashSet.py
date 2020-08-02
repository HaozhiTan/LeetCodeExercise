class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}  # dictionary or set

    def add(self, key: int) -> None:
        self.d[key] = 1

    def remove(self, key: int) -> None:
        if key in self.d:
            del self.d[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.d:
            return True
        else:
            return False


if __name__ == '__main__':
    # Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))
    print(obj.contains(3))
    obj.add(2)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.contains(2))
