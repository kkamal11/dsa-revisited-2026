class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0 or self.min[-1] >= val:
            self.min.append(val)

    def pop(self) -> None:
        el = self.stack.pop()
        if el == self.min[-1]:
            self.min.pop()
        return el

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


class MinStack2:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:

        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            last = self.stack[-1]
            self.stack.append([val, min(val, last[-1])])

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]
