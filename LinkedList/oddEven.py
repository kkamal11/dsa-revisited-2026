# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        L = []
        tmp = head
        while tmp and tmp.next:
            L.append(tmp.val)
            tmp = tmp.next.next
        if tmp:
            L.append(tmp.val)
        tmp = head.next
        while tmp and tmp.next:
            L.append(tmp.val)
            tmp = tmp.next.next
        if tmp:
            L.append(tmp.val)
        head = None
        for el in L:
            if head is None:
                head = ListNode(el)
                curr = head
            else:
                curr.next = ListNode(el)
                curr = curr.next
        return head

    def oddEvenListOptimized(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head

        return head
