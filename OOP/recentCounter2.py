class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        count = 0
        n = len(self.counter) - 1

        while n >= 0 and self.counter[n] >= (t - 3000):
            count += 1
            n -= 1

        return count


class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        self.counter = [log for log in self.counter if (t - 3000) <= log <= t]
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
