import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = collections.OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            self.d.move_to_end(key, last=True)
            return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key, last=True)
        self.d[key] = value
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)
        
if __name__ == "__main__":
# Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(2)
    # obj.put(1, 1)
    # obj.put(2, 2)
    # print(obj.get(1))
    # obj.put(3, 3)
    # print(obj.get(2))
    # obj.put(4, 4)
    # print(obj.get(1))
    # print(obj.get(3))
    # print(obj.get(4))
    obj.put(2, 1)
    obj.put(1, 1)
    obj.put(2, 3)
    obj.put(4, 1)
    print(obj.get(1))
    print(obj.get(2))

