class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 0

        self.stack.append(price)

        tmp_stack = self.stack.copy()

        while tmp_stack and tmp_stack[-1] <= price:
            count += 1
            tmp_stack.pop()

        return count


class StockSpannerOptimized:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span
