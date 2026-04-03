class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, val=None):
        self.head = Node(val)

    def insert_front(self, val):
        pass

    def insert_end(self, val):
        pass

    def delete(self, val):
        pass

    def display_forward(self):
        pass

    def display_backward(self):
        pass


# Example usage


def main():
    dll = DoublyLinkedList()
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_front(5)
    print("Forward:", dll.display_forward())  # Output: [5, 10, 20]
    print("Backward:", dll.display_backward())  # Output: [20, 10, 5]

    dll.delete(10)
    print("After deletion:")
    print("Forward:", dll.display_forward())  # Output: [5, 20]
    print("Backward:", dll.display_backward())  # Output: [20, 5]


if __name__ == "__main__":
    main()
