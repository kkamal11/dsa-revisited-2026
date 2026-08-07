class MyHashSet:

    def __init__(self):
        self.size = 10**5
        self.table = [-1] * self.size

    def _hash_idx(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash_idx(key)
        self.table[idx] = key

    def remove(self, key: int) -> None:
        idx = self._hash_idx(key)
        self.table[idx] = -1

    def contains(self, key: int) -> bool:
        idx = self._hash_idx(key)
        return self.table[idx] != -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSet:
    """
    Here is a simple implementation of a hash set using separate chaining for collision resolution.
    The hash set supports three main operations: add, remove, and contains.
    """

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        bucket = self.table[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        bucket = self.table[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key):
        return key in self.table[self._hash(key)]
