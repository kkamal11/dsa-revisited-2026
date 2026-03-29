# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        tmp = head
        seen = set()
        while tmp:
            if tmp in seen:
                return True
            seen.add(tmp)
            tmp = tmp.next
        return False


"""
Optimal Approach (Floyd's Cycle Detection)


Idea:
Use two pointers
slow → moves 1 step
fast → moves 2 steps
If cycle exists → they will meet
"""


def hasCycle(self, head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
