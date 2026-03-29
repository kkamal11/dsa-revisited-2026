class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_ll(head):
    tmp = head
    while tmp:
        print(tmp.data)
        tmp = tmp.next


def length_ll(head):
    count = 0
    tmp = head
    while tmp:
        count += 1
        tmp = tmp.next
    return count


def check_element(head, target):
    tmp = head
    while tmp:
        val = tmp.data
        if val == target:
            return True
        tmp = tmp.next
    return False


def delete_head(head):
    if head is None:
        return None
    print(f"{head.data} will be deleted")
    head = head.next
    return head


def delete_tail(head: Node):
    if head is None or head.next is None:
        return None
    tmp = head
    while tmp.next.next:
        tmp = tmp.next
    tmp.next = None
    return head


def delete_at_position_k(head, k):
    if head is None:
        return None
    tmp = head
    count = 1
    prev = tmp
    if k == 1:
        return head.next
    while tmp:
        if count == k:
            prev.next = tmp.next
            break
        count += 1
        prev = tmp
        tmp = tmp.next
    return head


def delete_by_value(head, val):
    if head is None:
        return None
    if head.data == val:
        return head.next
    tmp = head
    prev = head
    while tmp:
        link_val = tmp.data
        if link_val == val:
            prev.next = tmp.next
            break
        prev = tmp
        tmp = tmp.next
    return head


if __name__ == "__main__":
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

    print("length = ", length_ll(head))
    print(f"{12} present? {check_element(head, 12)}")
    print("beafore delete")
    print_ll(head)
    head = delete_head(head)
    print("after head delete")
    print_ll(head)
    print("tail delete")
    head = delete_tail(head)
    print_ll(head)
    print("-------------")
    head = delete_at_position_k(head, 4)
    print_ll(head)
    print("==========deleting by value======")
    head = delete_by_value(head, 12)
    print_ll(head)
