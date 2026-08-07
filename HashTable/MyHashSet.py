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
