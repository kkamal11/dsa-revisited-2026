# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return None
        total = 0
        tmp = head
        while tmp:
            total += 1
            tmp = tmp.next
        i = total - n + 1
        if i == 1:
            return head.next
        count = 0
        tmp = head
        prev = head
        while tmp:
            count += 1
            if count == i:
                prev.next = tmp.next if tmp.next else None
                break
            prev = tmp
            tmp = tmp.next
        return head
