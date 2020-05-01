class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_dict = {}
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.stack) == 1:
            self.min_dict[1] = x
        elif x < self.min_dict[len(self.stack)-1]:
            self.min_dict[len(self.stack)] = x
        else:
            self.min_dict[len(self.stack)] = self.min_dict[len(self.stack)-1]

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_dict[len(self.stack)]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-10)
    minStack.push(14)
    minStack.push(-20)
    print(minStack.getMin())
    minStack.pop()
    minStack.push(10)
    minStack.push(-7)
    minStack.push(-7)
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
    print(minStack.stack)
    print(minStack.min_dict)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()