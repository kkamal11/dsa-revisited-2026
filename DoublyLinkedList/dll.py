class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, val=None):
        if val is None:
            val = 0
        self.head = Node(val)

    def insert_front(self, val):
        new_node = Node(val)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node
        new_node.prev = tmp

    def delete(self, val):
        tmp = self.head
        # Head deletion
        if tmp.val == val:
            tmp.next.prev = None
            self.head = tmp.next
            return

        prev_node = None
        while tmp:
            if tmp.val == val:
                if tmp.prev is None:
                    # Head Deletion
                    self.head = tmp.next
                    if self.head:
                        self.head.prev = None
                else:
                    # Mid/tail element deletion
                    prev_node.next = tmp.next
                    if tmp.next:
                        tmp.next.prev = prev_node
                return
            prev_node = tmp
            tmp = tmp.next

    def display_forward(self):
        if self.head is None:
            return ""
        tmp = self.head
        L = []
        while tmp:
            L.append(tmp.val)
            tmp = tmp.next
        return " <-> ".join((str(x) for x in L))

    def display_backward(self):
        if self.head is None:
            return ""
        last = self.head
        while last.next:
            last = last.next
        L = []
        while last:
            L.append(last.val)
            last = last.prev
        return " <-> ".join((str(x) for x in L))


# Example usage


def main():
    dll = DoublyLinkedList()
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_front(5)
    dll.insert_end(25)
    dll.insert_end(35)
    print("Forward:", dll.display_forward())
    print("Backward:", dll.display_backward())

    dll.delete(35)
    print("\nAfter deletion")
    print("Forward:", dll.display_forward())
    print("Backward:", dll.display_backward())


if __name__ == "__main__":
    main()
