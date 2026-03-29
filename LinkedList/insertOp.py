class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_ll(head):
    tmp = head
    while tmp:
        print(tmp.data)
        tmp = tmp.next


head = Node(10)
third = Node(12)
fourth = Node(13)
fifth = Node(14)
sixth = Node(15)
second = Node(11, third)
head.next = second
third.next = fourth
fourth.next = fifth
fifth.next = sixth


def insert_at_head(head, node):
    if head is None:
        return node
    node.next = head
    return node


def insert_at_tail(head, node):
    if head is None:
        return node
    tmp = head
    while tmp:
        prev = tmp
        tmp = tmp.next
    prev.next = node
    return head


def insert_at_position_k(head, k, node):
    if head is None:
        return node
    if k == 1:
        node.next = head
        return node
    count = 1
    tmp = head
    prev = head
    while tmp:
        if count == k:
            prev.next = node
            node.next = tmp
        prev = tmp
        count += 1
        tmp = tmp.next
    return head


print_ll(head)
top = Node(9)
bottom = Node(16)
head = insert_at_head(head, top)
head = insert_at_tail(head, bottom)
print("========================")
print_ll(head)
print("========================random insert at k")
random = Node(999)
head = insert_at_position_k(head, 8, random)
print_ll(head)
