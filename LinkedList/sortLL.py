# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def fidMiddle(head: ListNode):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(head: ListNode):
        pass

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle = self.findMidle(head)
        left_head = head
        righ_head = middle
        middle.next = None
        left_head = self.sortList(left_head)
        righ_head = self.sortList(righ_head)

        return self.merge(left_head, righ_head)
