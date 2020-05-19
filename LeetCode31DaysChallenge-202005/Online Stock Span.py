class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


if __name__ == '__main__':
    S = StockSpanner()
    print(S.next(100))
    print(S.next(80))
    print(S.next(60))
    print(S.next(70))
    print(S.next(60))
    print(S.next(75))
    print(S.next(85))


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
