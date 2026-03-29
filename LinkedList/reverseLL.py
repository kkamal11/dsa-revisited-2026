# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        L = []
        tmp = head
        while tmp:
            val = tmp.val
            L.append(val)
            tmp = tmp.next
        first = L.pop()
        ans_head = ListNode(first)
        curr = ans_head
        while L:
            e = L.pop()
            curr.next = ListNode(e)
            curr = curr.next
        return ans_head


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        tmp = head
        prev = None
        while tmp:
            front = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = front
        return prev
