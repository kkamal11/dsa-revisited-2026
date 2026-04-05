class LRUCache:
    class Node:
        def __init__(self, _key, _val):
            self.key = _key
            self.val = _val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity
        self.m = {}

    def addNode(self, newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode

    def deleteNode(self, delNode):
        delPrev = delNode.prev
        delNext = delNode.next
        delPrev.next = delNext
        delNext.prev = delPrev

    def get(self, key_):
        if key_ in self.m:
            resNode = self.m[key_]
            res = resNode.val
            del self.m[key_]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.m[key_] = self.head.next
            return res
        return -1

    def put(self, key_, value):
        if key_ in self.m:
            existingNode = self.m[key_]
            del self.m[key_]
            self.deleteNode(existingNode)
        
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key_, value))
        self.m[key_] = self.head.next


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)

    print(cache.get(1))

    cache.put(3, 3)

    print(cache.get(2))

    cache.put(4, 4)

    print(cache.get(1))

    print(cache.get(3))

    print(cache.get(4))
