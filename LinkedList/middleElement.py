# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        total_element = 0
        tmp = head
        while tmp:
            total_element += 1
            tmp = tmp.next
        mid = total_element // 2
        tmp = head
        count = 0
        while tmp:
            if count == mid:
                return tmp
            count += 1
            tmp = tmp.next
        return tmp


class Solution2:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
