class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        curr = self.i
        while self.stack and self.stack[-1][0]<= price:
            item, ind = self.stack.pop()
            curr = ind
        self.stack.append((price,curr))
        self.i += 1
        return self.i - curr 


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)